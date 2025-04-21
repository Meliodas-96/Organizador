### Organizador de Archivos

Organizador de Archivos es una aplicación de escritorio para Windows que te permite organizar automáticamente los archivos de una carpeta en subcarpetas según su tipo (documentos, imágenes, música, videos, programas, comprimidos, código y otros). Incluye una interfaz gráfica sencilla y la opción de revertir los cambios realizados.

#### Características

- Interfaz gráfica intuitiva (Tkinter)
- Organización automática de archivos por extensión
- Registro de movimientos y posibilidad de revertir cambios
- Configuración personalizable mediante un archivo JSON
- Compatible con Windows

#### Instalación Recomendada 🚀

1. **Usar el archivo .exe (Recomendado)**
   - Simplemente descarga el archivo `Organizador.exe`
   - No requiere instalación de Python ni dependencias
   - Doble clic para ejecutar
   - ¡Listo para usar!

2. Alternativa para desarrolladores (usando Python)
   - Esta opción es solo si deseas modificar el código o contribuir al proyecto
   - Requiere Python 3.7 o superior
   - Instalar dependencias: `pip install -r requirements.txt`
   - Ejecutar: `python Organizador.py`

#### ¿Cómo funciona?

1. Abre la aplicación (ya sea el .exe o ejecutando el script).
2. Haz clic en "Seleccionar Carpeta" y elige la carpeta que deseas organizar.
3. El programa moverá los archivos a subcarpetas según su tipo.
4. Puedes revertir los cambios con el botón "Revertir Cambios".

#### Estructura de carpetas generada

- Documentos: .pdf, .docx, .xlsx, .pptx, .txt
- Imagenes: .jpg, .jpeg, .png", ".webp", ".gif", ".bmp", ".tiff", ".ico
- Videos: .mp4, .mov, .avi, ".avif", ".mkv", ".flv
- Musica: .mp3, .wav, ".flac", ".aac", ".ogg
- Programas: .exe, .msi, ".bat
- Comprimidos: .zip, ".rar", ".7z", ".tar", ".gz
- Codigo: .py, ".js", ".html", ".css", ".java", ".cpp
- Otros: Archivos sin extensión conocida

#### Archivos generados

- `C:/Temp/organizador.log`: Registro de actividad
- `C:/Temp/config.json`: Configuración de extensiones y carpetas
- `C:/Temp/movimientos.json`: Registro de movimientos para revertir cambios

#### Notas

- El icono de la aplicación debe estar en el mismo directorio que el ejecutable/script y llamarse `icono.ico`.
- El programa está pensado para Windows y utiliza la carpeta temporal `C:/Temp` para sus archivos de configuración y registro.

#### Licencia

Este proyecto es de uso libre. Si lo mejoras, ¡no dudes en hacer un pull request!