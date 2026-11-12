<p align="center">
  <img src="https://img.shields.io/badge/DESKTOP_APP-MATRIX_DOWNLOADER-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="Matrix Downloader"/>
  <img src="https://img.shields.io/badge/PYTHON-TKINTER-101010?style=for-the-badge&logo=python&logoColor=00FF41" alt="Python"/>
</p>

# Matrix Downloader

A local desktop application built with Python and Tkinter for managing audio and video downloads from individual URLs and playlists.

<p align="center">
  <a href="docs/index.html"><strong>SHOWCASE SOURCE</strong></a> ·
  <a href="https://github.com/tzayadet/matrix_downloader"><strong>SOURCE CODE</strong></a>
</p>

## Features

- Parses individual URLs and playlist entries.
- Allows selecting items before processing.
- Provides format and quality options.
- Runs processing tasks in the background to keep the interface responsive.
- Generates collision-resistant output names.
- Supports Windows executable packaging with PyInstaller.

## Requirements

- Python 3.10+
- FFmpeg
- Dependencies listed in [requirements.txt](requirements.txt)

## Run locally

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

**Linux / macOS**

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## Build for Windows

Run `MatrixDownloader_Build.bat` on Windows. The build process prepares the environment, installs dependencies and creates a portable executable.

## Project layout

| Path | Purpose |
|---|---|
| `main.py` | Desktop application entry point |
| `requirements.txt` | Python dependencies |
| `docs/` | Static project showcase |
| `tests/` | Automated tests |
| `MatrixDownloader_Build.bat` | Windows build launcher |

## Showcase and deployment

The static showcase source is available at [docs/index.html](docs/index.html). It presents the application and its workflow; it does not download, proxy or host media. GitHub Pages deployment is prepared but requires GitHub Pages to be enabled with GitHub Actions in repository settings and the `ENABLE_PAGES=true` Actions variable.

## Responsible use

Use the application only for content you are authorised to download. Follow platform terms and copyright rules. A publicly accessible URL does not automatically grant permission to copy or redistribute its content.

## Tests

```bash
python -m unittest discover -s tests -v
```

## License

See [LICENSE](LICENSE) for the repository's licensing terms.
