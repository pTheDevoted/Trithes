<div align="center">
  <p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/tool-CLI-green">
    <img alt="Static Badge" src="https://img.shields.io/badge/made_in-python-blue">
    <img src="images/trithes.png" width="300"/>
    <img alt="Static Badge" src="https://img.shields.io/badge/licence-MIT-red">
    <img alt="Static Badge" src="https://img.shields.io/badge/version-2.5.3-orange">
    <h1 align="center"><b>Trithes</b></h1>
</p>
</div>

# 🧭 Table of Contents

| Section | Description |
|--------|-------------|
| 📖 [About The Project](#-about-the-project) | Overview, context, and purpose |
| 📚 [Technologies and Libraries Used](#-technologies-and-libraries-used) | Libraries and technologies used |
| 🛠 [Core Features](#-core-features) | Key features and capabilities |
| 💻 [Compatibility](#-compatibility) | Tested platforms and stability |
| 🛠️ [Installation](#-installation) | Setup guide |
| 📄 [License](#-license) | Project licensing |
| 👤 [Contact](#-contact) | Developer contact info |

---

# 📖 About The Project
Trithes is a Python-based CLI tool for steganography and metadata analysis, allowing users to scan metadata from over 130 file formats, as well as insert and remove steganography in four formats.

This tool supports both interactive menu mode and command-line argument mode.
It enables:

- Embedding hidden messages into PNG, JPG, WEBP, and PDF files.

- Scanning metadata using ExifTool across a wide range of formats.

- Removing metadata in a clean and effective way.

- A portable forensic-style experience built for analysts, students, or hobbyists.

Visit the official site: https://pthedevoted.github.io/trithes-website

---

## 📚 Technologies and Libraries Used

| Technology | Description |
|:-----------|:------------|
| **Python (>=3.8)** | Core language |
| **ExifTool** | Metadata extraction and wiping |
| **Pillow (PIL)** | Embed metadata in PNG and WEBP |
| **piexif** | Handle EXIF data in JPEG/JPG |
| **argparse** | Parse command-line arguments |
| **subprocess** | Execute system commands |
| **shutil** | Terminal size and path detection |
| **os** | Filesystem operations |
| **rich** | CLI styling and formatting |
| **pystyle** | Terminal gradient effects |
| **InquirerPy** | Menu-style prompts |
| **PyPDF2** | Handle EXIF data in PDF |

---

# 🛠 Core Features

### 1. 📝 Message Embedding
Hide custom messages into:
- PNG/WEBP: `Pillow` custom fields
- JPG/JPEG: `Software` EXIF tag via `piexif`
- PDF: Insertion using `PyPDF2`

### 2. 🔍 Metadata Scanning
- Scan metadata from over **130+ file formats**
- Based on `exiftool`, with automatic filtering and formatting

### 3. 🧹 Metadata Wipe
- Removes metadata from supported formats (JPG, PNG, WEBP, PDF)
- Uses clean rewrite techniques or library-specific removals

### 4. ⚙️ Dual Interface (Menu + CLI)
- **Menu mode** for beginners
- **Argument mode** for advanced use cases, automation, scripting

### 5. 📋 Error Resilience
- Detects invalid formats
- Friendly error feedback
- Non-destructive file handling

### 6. 💻 Professional UX
- Command line interface with consistent messaging
- A professional terminal experience
  
---

# 💻 Compatibility

| Platform | Status |
|----------|--------|
| **Ubuntu** | ✅ Fully stable |
| **macOS** | ✅ Fully stable |
| **Termux** | ⚠️ Partial support: some dependencies may require manual setup |

---


# 🛠️ Installation
> [!NOTE]
> For the installation to work, you must have git installed previously.
```
git clone https://github.com/pTheDevoted/Trithes
```
```
cd Trithes
```
```
bash install.sh
```
(After installation, it automatically starts in menu mode)
## 📡 Start in menu mode (recommended for beginners)
Use the command ↓ to start the python virtual environment
```
source trithes_env/bin/activate
```
And use ↓ to start
```
python3 trithes.py
```
After use, the user ↓ to close the virtual environment (recommended)
```
deactivate
```
---

## 📡 Start in argument mode (recommended for experienced)
Use the command ↓ to start the python virtual environment
```
source trithes_env/bin/activate
```
And use ↓ to get the list of arguments
```
python3 trithes.py -h
```
After use, the user ↓ to close the virtual environment (recommended)
```
deactivate
```
---

# 📄 License
This project is licensed under the MIT License © 2025 Pedro-A.

---

# 👤 Contact

Discord: thedevoted

Instagram: @pedrodevoted
