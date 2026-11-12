# Matrix Downloader

A local desktop application built with Python and Tkinter for managing audio and video downloads from individual URLs and playlists.

<p align="center">
  <a href="https://github.com/tzayadet/matrix_downloader"><img src="https://img.shields.io/badge/SOURCE-GITHUB-161b22?style=flat-square&logo=github" alt="Source code"></a>
  <a href="docs/index.html"><img src="https://img.shields.io/badge/SHOWCASE-SOURCE-00a86b?style=flat-square" alt="Showcase source"></a>
</p>

## Features

- Parses individual URLs and playlist entries.
- Allows selecting items before processing.
- Provides format and quality options.
- Runs processing tasks in the background to keep the interface responsive.
- Generates collision-resistant output names.
- Supports Windows executable packaging with PyInstaller.

## Requirements

- Python 3.10 or later.
- FFmpeg.
- Dependencies listed in [requirements.txt](requirements.txt).

## Run locally

Create and activate a virtual environment.

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

Run `MatrixDownloader_Build.bat` on Windows. The build process prepares the environment, installs the required dependencies and creates a portable executable.

## Project structure

| Path | Purpose |
|---|---|
| `main.py` | Desktop application entry point |
| `requirements.txt` | Python dependencies |
| `docs/` | Static project showcase |
| `tests/` | Automated tests |
| `MatrixDownloader_Build.bat` | Windows build launcher |

## Showcase and deployment

The static showcase source is available in [docs/index.html](docs/index.html). It presents the application and its workflow; it does not download, proxy or host media. GitHub Pages is not currently confirmed as published for this repository.

To publish it, enable GitHub Pages with GitHub Actions in repository settings and run the Pages workflow.

## Responsible use

Use the application only for content you are authorized to download. Follow the applicable platform terms and copyright rules. A publicly accessible URL does not automatically grant permission to copy or redistribute its content.

## Tests

```bash
python -m unittest discover -s tests -v
```

## License

See [LICENSE](LICENSE) for the repository's licensing terms.
