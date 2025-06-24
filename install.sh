#!/bin/bash

b="\033[0m"
v1="${b}\033[32m"
r1="${b}\033[31m"

clear
echo -e "${r1}\nDetecting environment...\n"

# Verifica SO
OS=$(uname -o)
DISTRO=""

if [ "$OS" == "Android" ]; then
    echo -e "${b}[${v1}+${b}] Termux environment detected.\n"
    DISTRO="Termux"
elif [ -f /etc/os-release ]; then
    . /etc/os-release
    if [[ "$ID" == "kali" ]]; then
        echo -e "${b}[${v1}+${b}] Kali Linux environment detected.\n"
        DISTRO="Kali"
    elif [[ "$ID" == "ubuntu" ]]; then
        echo -e "${b}[${v1}+${b}] Ubuntu environment detected.\n"
        DISTRO="Ubuntu"
    else
        echo -e "${b}[${r1}!${b}] Unknown Linux distribution: $ID. Exiting..."
        exit 1
    fi
else
    echo -e "${b}[${r1}!${b}] Unknown environment. Exiting..."
    exit 1
fi

# Instala dependências do sistema
if [ "$DISTRO" == "Termux" ]; then
    pkg update -y && pkg install -y libjpeg-turbo pcre libpng zlib python python-pip virtualenv exiftool
elif [ "$DISTRO" == "Kali" ] || [ "$DISTRO" == "Ubuntu" ]; then
    sudo apt update -y && sudo apt install -y \
        libjpeg-dev libpng-dev zlib1g-dev \
        python3-pip python3-venv libimage-exiftool-perl
fi

echo -e "${b}[${v1}+${b}] Creating Python virtual environment..."

if [ "$DISTRO" == "Termux" ]; then
    python -m venv trithes_env
    source trithes_env/bin/activate
else
    python3 -m venv trithes_env
    source trithes_env/bin/activate
fi

echo -e "${b}[${v1}+${b}] Virtual environment activated."

# Instala dependências Pythonnn
echo -e "${b}[${v1}+${b}] Installing required Python libraries..."
pip install --upgrade pip
pip install pillow pystyle piexif InquirerPy rich PyPDF2

# Verifica instalação do ExifTool
if ! command -v exiftool &> /dev/null; then
    echo -e "${b}[${r1}!${b}] exiftool not found! Please check the installation."
    exit 1
else
    echo -e "${b}[${v1}+${b}] exiftool successfully installed!"
fi

# Executa o programa
echo -e "${b}[${v1}+${b}] Launching Trithes...\n"
python3 trithes.py
