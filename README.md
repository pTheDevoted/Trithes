
<div align="center">

  <p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/tool-CLI-green">
    <img alt="Static Badge" src="https://img.shields.io/badge/make_in-python-blue">
    <img src="images/trithes.png" width="300"/>
    <img alt="Static Badge" src="https://img.shields.io/badge/licence-MIT-red">
    <img alt="Static Badge" src="https://img.shields.io/badge/version-1.0.0-orange">
    <h1 align="center"><b>Trithes</b></h1>
</p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">📖 About The Project</a>
      <ul>
        <li><a href="#technologies-and-libraries-used">📚 Technologies and Libraries Used</a></li>
      </ul>
    </li>
    <li><a href="#core-features">🛠 Core Features</a></li>
        <li>
      <a href="#installation-and-usage">🛠️ Installation And Usage</a>
      <ul>
        <li><a href="#start-in-kali-linux-and-termux">📡 Start in Kali Linux and Termux</a></li>
      </ul>
      <ul>
        <li><a href="#start-in-ubuntu">📡 Start in Ubuntu/a></li>
      </ul>
    </li>
    <li><a href="#license">📄 License</a></li>
    <li><a href="#contact">👤 Contact</a></li>
  </ol>
</details>

---

# 📖 About The Project
Trithes is a Python command-line tool that uses steganography to hide and extract messages in images. With scan capabilities to detect hidden data and hide to discreetly embed messages, Trithes employs advanced bit manipulation techniques, ensuring high efficiency and image integrity.

This project provides a sleek and functional interface for metadata manipulation in image files (.jpg, .jpeg, .png, .webp).  
It allows you to:

- Embed hidden messages within image metadata.
- Perform full metadata scans.
- Safely wipe hidden or sensitive information.
- Maintain a refined and intuitive user experience via the command line.

The application integrates robust image-processing technologies and professional-grade forensic tools.



## 📚 Technologies and Libraries Used

| Technology | Description |
|:-----------|:------------|
| **Python (>=3.8)** | Primary development language. |
| **Pillow (PIL)** | Image processing and metadata editing for PNG/WEBP. |
| **piexif** | Insertion and editing of EXIF metadata for JPEG/JPG. |
| **ExifTool** | Industry-standard CLI tool for metadata handling. |
| **subprocess** | Execution and management of external processes. |
| **os** | File system operations and validations. |
| **pystyle** | Advanced CLI output styling. |

---

# 🛠 Core Features

### 1. Message Embedding
Hides a user-defined string into the image metadata:
- PNG/WEBP: Uses custom fields (Hidden Message) via **Pillow**.
- JPEG/JPG: Inserts into the Software EXIF tag via **piexif**.

### 2. Metadata Scanning
Performs a comprehensive scan of embedded metadata using:
- **ExifTool** as the scanning engine, ensuring maximum compatibility and precision.

### 3. Metadata Cleaning
Securely removes all embedded metadata by:
- Executing `exiftool -all=`, ensuring complete metadata wipe.

### 4. Manual EXIF Decoding
Utilizes **piexif** to manually extract and decode EXIF tags from JPEG/JPG files.

### 5. Error Handling and Resilience
- Rigorous validation of formats and paths.
- Robust exception management for expected and unexpected errors.
- Integrity-preserving operations to prevent file corruption.

### 6. User Interface Experience
- Automatic color styling for friendly, informative feedback.
- Consistent and polished messaging for a professional terminal experience.

---

# 🛠️ Installation And Usage
> [!NOTE]
> For the installation to work, you must have git and python installed previously.
```
git clone https://github.com/pTheDevoted/Trithes
```
```
cd Trithes
```
```
bash install.sh
```
## 📡 Start in Kali Linux and Termux
Use the command ↓
```
python3 trithes.py
```
To start the program whenever you want

## 📡 Start in Ubuntu
Use the command ↓ to start the python virtual environment
```
source trithes_env/bin/activate
```
And use ↓ to start
```
python3 trithes.py
```

---

# 📄 License
This project is licensed under the [MIT License](./LICENSE) © 2025 Pedro-A.

---

# 👤 Contact
Discord: thedevoted

Instagram: pedrodevoted
