import os
import shutil
import logging
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Button

# Configurar logging
temp_dir = "C:/Temp"  # Cambia la ruta a C:/Temp
os.makedirs(temp_dir, exist_ok=True)  # Crear la carpeta C:/Temp si no existe

logging.basicConfig(
    filename=os.path.join(temp_dir, "organizador.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def cargar_configuracion():
    """Carga las configuraciones desde un archivo JSON."""
    config_path = os.path.join(temp_dir, "config.json")
    if not os.path.exists(config_path):
        configuracion = {
            "subcarpetas": {
                "Documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
                "Imagenes": [".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff", ".ico"],
                "Videos": [".mp4", ".mov", ".avi", ".avif", ".mkv", ".flv"],
                "Musica": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
                "Programas": [".exe", ".msi", ".bat"],
                "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
                "Codigo": [".py", ".js", ".html", ".css", ".java", ".cpp"],
                "Otros": []  # Archivos sin extensión conocida
            }
        }
        with open(config_path, "w") as f:
            json.dump(configuracion, f, indent=4)
        logging.info("Archivo de configuración creado: config.json")
    else:
        with open(config_path, "r") as f:
            configuracion = json.load(f)
    return configuracion

def registrar_movimientos(movimientos):
    """Registra los movimientos en un archivo de registro."""
    registro_path = os.path.join(temp_dir, "movimientos.json")
    with open(registro_path, "w") as f:
        json.dump(movimientos, f, indent=4)
    logging.info("Movimientos registrados en movimientos.json")

def organizar_archivos_gui(ruta_base, progressbar, status_label):
    configuracion = cargar_configuracion()
    subcarpetas = configuracion.get("subcarpetas", {})

    if not os.path.exists(ruta_base):
        messagebox.showerror("Error", f"La carpeta {ruta_base} no existe.")
        return

    archivos = [archivo for archivo in os.listdir(ruta_base) if os.path.isfile(os.path.join(ruta_base, archivo))]
    movimientos = []

    progressbar["maximum"] = len(archivos)
    progressbar["value"] = 0

    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_base, archivo)
        extension = os.path.splitext(archivo)[1].lower()
        movido = False

        for subcarpeta, extensiones in subcarpetas.items():
            if extension in extensiones:
                carpeta_destino = os.path.join(ruta_base, subcarpeta)
                os.makedirs(carpeta_destino, exist_ok=True)
                try:
                    shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                    logging.info(f"Movido: {archivo} -> {subcarpeta}")
                    movimientos.append({"archivo": archivo, "destino": subcarpeta, "origen": ruta_base})
                    movido = True
                except Exception as e:
                    logging.error(f"Error al mover {archivo} a {subcarpeta}: {e}")
                break

        if not movido:
            carpeta_destino = os.path.join(ruta_base, "Otros")
            os.makedirs(carpeta_destino, exist_ok=True)
            try:
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                logging.info(f"Movido: {archivo} -> Otros")
                movimientos.append({"archivo": archivo, "destino": "Otros", "origen": ruta_base})
            except Exception as e:
                logging.error(f"Error al mover {archivo} a Otros: {e}")

        progressbar["value"] += 1
        progressbar.update()

    registrar_movimientos(movimientos)
    status_label["text"] = "Organización completada."
    messagebox.showinfo("Completado", "Organización completada.")

def revertir_cambios():
    registro_path = os.path.join(temp_dir, "movimientos.json")
    if not os.path.exists(registro_path):
        messagebox.showerror("Error", "No hay movimientos registrados para revertir.")
        return

    with open(registro_path, "r") as f:
        movimientos = json.load(f)

    for movimiento in movimientos:
        archivo = movimiento["archivo"]
        subcarpeta = movimiento["destino"]
        origen = movimiento["origen"]
        ruta_origen = os.path.join(origen, subcarpeta, archivo)
        ruta_destino = os.path.join(origen, archivo)

        if os.path.exists(ruta_origen):
            try:
                shutil.move(ruta_origen, ruta_destino)
                logging.info(f"Revertido: {archivo} de {subcarpeta} a {origen}")
            except Exception as e:
                logging.error(f"Error al revertir {archivo}: {e}")

    os.remove(registro_path)
    messagebox.showinfo("Revertir", "Cambios revertidos con éxito.")

def seleccionar_carpeta(progressbar, status_label):
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta")
    if carpeta:
        organizar_archivos_gui(carpeta, progressbar, status_label)

def interfaz_grafica():
    root = tk.Tk()
    root.title("Organizador de Archivos")
    root.geometry("500x300")
    root.configure(bg="#f0f0f0")
    root.iconbitmap(os.path.join(os.path.dirname(__file__), "icono.ico"))

    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=20)

    title = tk.Label(frame, text="Organizador de Archivos", font=("Arial", 16, "bold"), bg="#f0f0f0")
    title.pack(pady=10)

    tk.Label(frame, text="Seleccione la carpeta a organizar:", bg="#f0f0f0").pack(pady=5)

    progressbar = Progressbar(frame, orient="horizontal", length=400, mode="determinate")
    progressbar.pack(pady=10)

    status_label = tk.Label(frame, text="", bg="#f0f0f0")
    status_label.pack(pady=5)

    buttons_frame = tk.Frame(frame, bg="#f0f0f0")
    buttons_frame.pack(pady=10)

    seleccionar_btn = Button(buttons_frame, text="Seleccionar Carpeta", command=lambda: seleccionar_carpeta(progressbar, status_label))
    seleccionar_btn.grid(row=0, column=0, padx=5)

    revertir_btn = Button(buttons_frame, text="Revertir Cambios", command=revertir_cambios)
    revertir_btn.grid(row=0, column=1, padx=5)

    salir_btn = Button(buttons_frame, text="Salir", command=root.quit)
    salir_btn.grid(row=0, column=2, padx=5)

    root.mainloop()

if __name__ == "__main__":
    interfaz_grafica()