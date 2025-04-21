# 🗂️ **Organizador de Archivos** 📁✨

¡Bienvenido/a! 🙌

**Organizador de Archivos** es una aplicación de escritorio para **Windows** que te ayuda a mantener tus carpetas limpias y ordenadas **automáticamente**. Organiza tus documentos, imágenes, música, videos, programas y más con **un solo clic**. Ideal para quienes aman el orden y la productividad. 🚀

---

## 🧑‍💻 **Características**

- **Interfaz gráfica intuitiva** (desarrollada con Tkinter).
- **Organización automática** de archivos por tipo de extensión.
- **Registro de movimientos** y posibilidad de **revertir cambios**.
- **Configuración personalizable** mediante un archivo JSON.
- **Compatible con Windows**.

---

## 📦 **Instalación**

### **Opción Fácil** (Recomendada)
1. Descarga el archivo `Organizador.exe` desde la sección de **Releases**.
2. No necesitas instalar **Python** ni dependencias.
3. ¡Haz doble clic y listo para usar! 🎉

### **Opción para Desarrolladores**
1. Asegúrate de tener **Python 3.7+** instalado.
2. Clona o descarga este repositorio.
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Ejecuta el script:
    ```bash
    python Organizador.py
    ```

---

## ⚙️ **¿Cómo funciona?**

1. Abre la aplicación.
2. Haz clic en **"Seleccionar Carpeta"** y elige la carpeta que deseas organizar.
3. El programa moverá los archivos a **subcarpetas** según su tipo.
4. ¿Te arrepentiste? Haz clic en **"Revertir Cambios"** para deshacer la organización.

---

## 📂 **Tipos de archivos organizados**

| **Carpeta**      | **Extensiones**                                                   |
|------------------|--------------------------------------------------------------------|
| 📄 **Documentos** | `.pdf`, `.docx`, `.xlsx`, `.pptx`, `.txt`                          |
| 🖼️ **Imágenes**   | `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, `.bmp`, `.tiff`, `.ico`  |
| 🎬 **Videos**     | `.mp4`, `.mov`, `.avi`, `.avif`, `.mkv`, `.flv`                    |
| 🎵 **Música**     | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`                            |
| 💾 **Programas**  | `.exe`, `.msi`, `.bat`                                             |
| 📦 **Comprimidos**| `.zip`, `.rar`, `.7z`, `.tar`, `.gz`                               |
| 💻 **Código**     | `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`                     |
| ❓ **Otros**      | Archivos sin extensión conocida                                    |

---

## 📝 **Archivos generados**

- **`C:/Temp/organizador.log`**: Registro de actividad.
- **`C:/Temp/config.json`**: Configuración de extensiones y carpetas.
- **`C:/Temp/movimientos.json`**: Registro de movimientos para revertir cambios.

---

## 🛠️ **Notas**

- El **icono de la aplicación** debe llamarse `icono.ico` y estar en el mismo directorio que el ejecutable o script.
- El programa está diseñado para **Windows** y utiliza la carpeta temporal **C:/Temp** para sus archivos de configuración y registro.

---

## 📝 **Licencia**

Este proyecto está bajo la **licencia MIT**. ¡Si lo mejoras o tienes alguna sugerencia, no dudes en hacer un **pull request**! Ver archivo [LICENSE](LICENSE).

---

## 🌟 **¡Colabora y comparte!**

¿Te gustó la app? 
- Dale una **estrella** ⭐.
- ¡Compártela con tus amigos o colegas!
- **Contribuye** con ideas, mejoras o correcciones.

¡Tu **feedback** es siempre bienvenido! 😄

---

Gracias por usar **Organizador de Archivos**. ¡Que disfrutes del orden! ✨
