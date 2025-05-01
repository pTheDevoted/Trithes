#!/bin/bash

# Cores.
b="\033[0m"
v1="\033[32m"
r1="\033[31m"

clear

echo -e "${r1}\nDetecting environment...\n${b}"

OS=$(uname -o)
DISTRO=""

if [ "$OS" == "Android" ]; then
    echo -e "[${v1}+${b}] Termux environment detected.\n"
    DISTRO="Termux"
elif [ -f /etc/os-release ]; then
    . /etc/os-release
    if [[ "$ID" == "kali" ]]; then
        echo -e "[${v1}+${b}] Kali Linux environment detected.\n"
        DISTRO="Kali"
    elif [[ "$ID" == "ubuntu" ]]; then
        echo -e "[${v1}+${b}] Ubuntu environment detected.\n"
        DISTRO="Ubuntu"
    else
        echo -e "[${r1}!${b}] Unknown Linux distribution: $ID. Exiting..."
        exit 1
    fi
else
    echo -e "[${r1}!${b}] Unknown environment. Exiting..."
    exit 1
fi

# Instalação das dependências.
if [ "$DISTRO" == "Termux" ]; then
    pkg update -y && pkg install -y libjpeg-turbo pcre libpng zlib python3 exiftool
else
    sudo apt update -y && sudo apt install -y \
        libjpeg-dev libpng-dev zlib1g-dev python3-pip python3-venv libimage-exiftool-perl

    # Ambiente virtual.
    python3 -m venv trithes_env
    source trithes_env/bin/activate
fi

# Instalação de bibliotecas python.
pip3 install --upgrade pip
pip3 install pillow pystyle piexif InquirerPy

# Verificação do exiftool
if ! command -v exiftool &> /dev/null; then
    echo -e "[${r1}!${b}] exiftool not found! Please check installation."
    exit 1
else
    echo -e "[${v1}+${b}] All ok!"
fi

echo -e "[${v1}+${b}] Starting the program...\n"
python3 trithes.py
