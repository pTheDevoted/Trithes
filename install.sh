#!/bin/bash

set -e

YELLOW='\033[1;33m'
GREEN='\033[1;32m'
RED='\033[1;31m'
NC='\033[0m' # Sem cor

VENV_DIR="trithes_env"

echo -e "${YELLOW}[*] Detecting operating system...${NC}"

OS="$(uname -s)"
case "$OS" in
    Linux)
        if [ -n "$ANDROID_ROOT" ]; then
            PLATFORM="termux"
            echo -e "${GREEN}[+] Platform detected: Termux (Android)${NC}"
        else
            PLATFORM="linux"
            echo -e "${GREEN}[+] Platform detected: Debian-based Linux (apt)${NC}"
        fi
        ;;
    Darwin)
        PLATFORM="macos"
        echo -e "${GREEN}[+] Platform detected: macOS${NC}"
        ;;
    *)
        echo -e "${RED}[!] Unsupported system: $OS${NC}"
        exit 1
        ;;
esac

echo -e "${YELLOW}[*] Checking for Python and pip...${NC}"

if command -v python3 &> /dev/null; then
    PYTHON=python3
else
    echo -e "${RED}[!] Python 3 not found. Please install it manually.${NC}"
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo -e "${YELLOW}[*] pip3 not found. Installing...${NC}"
    case "$PLATFORM" in
        linux)
            sudo apt update && sudo apt install -y python3-pip
            ;;
        macos)
            brew install python
            ;;
        termux)
            pkg update && pkg install -y python
            ;;
    esac
fi

echo -e "${YELLOW}[*] Creating virtual environment...${NC}"
$PYTHON -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

if [ ! -f "$VENV_DIR/bin/activate" ]; then
    echo -e "${RED}[!] Failed to create virtual environment.${NC}"
    exit 1
fi

echo -e "${YELLOW}[*] Installing Python dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${YELLOW}[*] Checking for ExifTool (system-wide)...${NC}"

if ! command -v exiftool &> /dev/null; then
    echo -e "${YELLOW}[!] ExifTool not found. Installing...${NC}"
    case "$PLATFORM" in
        linux)
            sudo apt install -y libimage-exiftool-perl
            ;;
        macos)
            brew install exiftool
            ;;
        termux)
            echo -e "${RED}[!] ExifTool is not available by default in Termux.${NC}"
            echo -e "${RED}    You can try installing with:${NC} cpan Image::ExifTool"
            echo -e "${RED}    Or compile it manually from source.${NC}"
            ;;
    esac
else
    echo -e "${GREEN}[✓] ExifTool is already installed.${NC}"
fi

echo -e "${GREEN}[✓] Setup completed successfully!${NC}"
echo -e "${YELLOW}[i] To activate the environment, run: source $VENV_DIR/bin/activate${NC}"
