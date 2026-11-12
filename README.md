# Matrix Downloader

Aplicación de escritorio local desarrollada con Python y Tkinter para gestionar descargas de audio y vídeo desde URLs individuales y playlists.

**Project showcase:** [Open the project page](https://tzayadet.github.io/matrix_downloader/) · [Showcase source](docs/index.html)

## Funcionalidades

- Análisis de URLs individuales y playlists.
- Selección individual de elementos antes de procesarlos.
- Opciones de formato y calidad.
- Procesamiento en segundo plano para mantener la interfaz receptiva.
- Nombres de salida anti-colisión para evitar sobrescrituras.
- Compilación de un ejecutable Windows mediante PyInstaller.

## Requisitos

- Python 3.10 o superior.
- FFmpeg.
- Dependencias de [requirements.txt](requirements.txt).

## Ejecutar desde código fuente

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

Linux / macOS:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## Compilar para Windows

Ejecuta `MatrixDownloader_Build.bat` en Windows. El proceso prepara el entorno de compilación, obtiene las dependencias necesarias y genera el ejecutable portable.

## Pruebas

```bash
python -m unittest discover -s tests -v
```

## Uso responsable

La página de presentación no descarga ni aloja contenido. Utiliza la aplicación únicamente con contenido que tengas derecho a descargar y respeta las condiciones de uso de cada plataforma. No se debe asumir que una URL pública autoriza cualquier copia o redistribución.

## Showcase

Para publicar la página, activa GitHub Pages en **Settings → Pages → Build and deployment → Source → GitHub Actions** y ejecuta el workflow de publicación desde Actions.

## Licencia

Consulta [LICENSE](LICENSE).
