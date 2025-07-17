import os
import subprocess
import shutil
from PIL import Image, PngImagePlugin
import piexif
import display
from PyPDF2 import PdfReader, PdfWriter

def run_exiftool(args):
    exiftool_path = shutil.which("exiftool")
    if not exiftool_path:
        print(f"{display.red}[!] ExifTool not found in PATH.")
        print(f"{display.yellow}    Please install it using: apt install exiftool, brew install exiftool, or cpan Image::ExifTool")
        return None

    try:
        result = subprocess.run([exiftool_path] + args, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"{display.red}[!] Error running exiftool: {e}")
        return None

def hide_message(file_path, message):
    try:
        if file_path.endswith(".png"):
            img = Image.open(file_path)
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("Hidden Message", message)
            img.save(file_path, pnginfo=metadata)

        elif file_path.endswith((".jpg", ".jpeg")):
            exif_dict = {"0th": {piexif.ImageIFD.Software: message}}
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, file_path)

        elif file_path.endswith(".webp"):
            img = Image.open(file_path)
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("Hidden Message", message)
            img.save(file_path, "WEBP", pnginfo=metadata)

        elif file_path.endswith(".pdf"):
            reader = PdfReader(file_path)
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            metadata = reader.metadata or {}
            metadata.update({"/Title": message})
            writer.add_metadata(metadata)

            with open(file_path, "wb") as f_out:
                writer.write(f_out)

        else:
            print(f"\n{display.red}[!] Unsupported file format for hiding messages.")
            return False

        return True
    except Exception as e:
        print(f"\n{display.red}[!] Error while hiding message: {e}")
        return False

def scan_image_metadata(file_path):
    if not os.path.isfile(file_path):
        print(f"\n{display.red}[!] Invalid file path provided.")
        return

    print(f"Scanning metadata for {file_path}...")

    output = run_exiftool([file_path])

    if output:
        lines = output.splitlines()
        filtered = "\n".join(line for line in lines if "ExifTool Version Number" not in line)
        print(f"\n{display.yellow}Metadata found:\n{display.white}{filtered}")
    else:
        print(f"{display.red}[!] Unable to scan metadata or unsupported file.")

def remove_metadata(file_path):
    try:
        if file_path.endswith((".jpg", ".jpeg")):
            piexif.remove(file_path)
            print(f"\n{display.green}[+] Metadata removed from {file_path}")

        elif file_path.endswith(".png"):
            img = Image.open(file_path)
            img.save(file_path)
            print(f"\n{display.green}[+] Metadata removed from {file_path}")

        elif file_path.endswith(".pdf"):
            reader = PdfReader(file_path)
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.add_metadata({})
            with open(file_path, "wb") as f:
                writer.write(f)
                print(f"\n{display.green}[+] Metadata removed from {file_path}")

        else:
            print(f"\n{display.red}[!] Unsupported file format for metadata removal.")
    except Exception as e:
        print(f"\n{display.red}[!] Error removing metadata: {e}")

VERSION = "2.5.3"
