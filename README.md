<div align="center">
  <p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/tool-CLI-green">
    <img alt="Static Badge" src="https://img.shields.io/badge/made_in-python-blue">
    <img src="images/trithes.png" width="300"/>
    <img alt="Static Badge" src="https://img.shields.io/badge/licence-MIT-red">
    <img alt="Static Badge" src="https://img.shields.io/badge/version-2.0.0-orange">
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

Trithes is a Python-based CLI tool for **steganography and metadata analysis**, allowing users to embed, inspect, or wipe metadata from over **130 file formats**.

This tool supports both **interactive mode (menu)** and **advanced terminal mode** with arguments. It allows:

- Embedding secret messages in PNG, JPG, WEBP, and even PDF.
- Scanning metadata from virtually any format supported by ExifTool.
- Full metadata wipe functionality.
- Fast and accessible forensic-style usage for both analysts and curious users.

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
| **os** | Filesystem operations |
| **rich** | CLI styling and formatting |
| **pystyle** | Terminal gradient effects |
| **InquirerPy** | Menu-style prompts |

---

# 🛠 Core Features

### 1. 📝 Message Embedding
Hide custom messages into:
- PNG/WEBP: `Pillow` custom fields
- JPG/JPEG: `Software` EXIF tag via `piexif`
- PDF: Insertion using ExifTool

### 2. 🔍 Metadata Scanning
- Scan metadata from over **130+ file formats**
- Based on `exiftool`, with automatic filtering and formatting

### 3. 🧹 Metadata Wipe
- Uses `exiftool -all=` to clean all metadata from any file

### 4. ⚙️ Dual Interface (Menu + CLI)
- **Menu mode** for beginners
- **Argument mode** for advanced users and scripting

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
| **Kali Linux** | ⚠️ Stable, but ExifTool must be preinstalled |
| **Termux** | ⚠️ Limited, may require manual setup of dependencies |

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
