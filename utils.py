import os
import subprocess
from PIL import Image, PngImagePlugin
import piexif
import display
from PyPDF2 import PdfReader, PdfWriter


def run_exiftool(args):
    try:
        result = subprocess.run(['/usr/bin/exiftool'] + args, capture_output=True, text=True)
        return result.stdout.strip()
    except FileNotFoundError:
        print(f"{display.red}[!] ExifTool not found.")
        return None
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
            input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
            return False

        return True
    except Exception as e:
        print(f"\n{display.red}[!] Error while hiding message: {e}")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
        return False


def scan_image_metadata(file_path):
    if not os.path.isfile(file_path):
        print(f"\n{display.red}[!] The provided path is not a valid file.")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
        return

    print(f"Scanning metadata for {file_path}...")

    output = run_exiftool([file_path])

    if output:
        lines = output.splitlines()
        filtered = "\n".join(line for line in lines if "ExifTool Version Number" not in line)
        print(f"\n{display.yellow}Metadata found:\n{display.white}{filtered}")
    else:
        print(f"{display.red}[!] Could not scan metadata or file not supported.")

    input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")


VERSION = "2.0.0"
