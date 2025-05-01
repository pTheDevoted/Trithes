import os
import subprocess
import time
from PIL import Image, PngImagePlugin
import piexif
import display
from pystyle import Colorate, Colors


def run_exiftool(args):
    try:
        # Run exiftool command with args
        result = subprocess.run(['/usr/bin/exiftool'] + args, capture_output=True, text=True)
        return result.stdout.strip()  # Return the output of the command
    except FileNotFoundError:
        print(f"{display.red}[!] ExifTool not found in the project directory. Please ensure it's installed.")
        return None
    except Exception as e:
        print(f"{display.red}[!] Error running exiftool: {e}")
        return None


def hide_message(image_path, message):
    try:
        if image_path.endswith(".png"):
            img = Image.open(image_path)
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("Hidden Message", message)
            img.save(image_path, pnginfo=metadata)
        elif image_path.endswith((".jpg", ".jpeg")):
            exif_dict = {"0th": {piexif.ImageIFD.Software: message}}
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, image_path)
        elif image_path.endswith(".webp"):
            img = Image.open(image_path)
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("Hidden Message", message)
            img.save(image_path, "WEBP", pnginfo=metadata)
        else:
            print(f"\n{display.red}[!] Invalid file format.")
            input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
            return

        print(f'\n{display.green}Hidden message successfully added to {image_path}!')
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
    except FileNotFoundError:
        print(f"\n{display.red}[!] File not found")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
    except Exception as e:
        print(f"\n{display.red}[!] An error occurred (report this error to the creator): {e}")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")


def decode_exif(exif_bytes):
    exif_data = piexif.load(exif_bytes)
    exif_info = {}
    for ifd in exif_data:
        if exif_data[ifd] is not None:
            for tag in exif_data[ifd]:
                tag_name = piexif.TAGS[ifd][tag]["name"]
                value = exif_data[ifd][tag]
                if isinstance(value, bytes):
                    try:
                        value = value.decode("utf-8", errors="ignore")
                    except UnicodeDecodeError:
                        value = value.decode("latin1", errors="ignore")
                exif_info[tag_name] = value
    return exif_info


def scan_image_metadata(image_path):
    if not os.path.isfile(image_path):
        print(f"\n{display.red}[!] The provided path is not a valid file.")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
        return

    if not image_path.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        print(f"\n{display.red}[!] Unsupported file format.")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
        return

    print(f"Scanning metadata for {image_path}...")

    output = run_exiftool([image_path])

    if output:
        # Filter out the ExifTool version line
        output_lines = output.splitlines()
        filtered_output = "\n".join(line for line in output_lines if "ExifTool Version Number" not in line)
        print(f"\n{display.yellow}Metadata found:\n{display.white}{filtered_output}")
    else:
        print("[!] Could not scan metadata.")

    # Wait for user input before continuing
    input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")


def clear_metadata(image_path):
    if not os.path.isfile(image_path):
        print(f"\n{display.red}[!] File not found.")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
        return

    if image_path.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        print(f"\n{display.yellow}Clearing metadata for {image_path}...")
        output = run_exiftool(['-all=', image_path])

        if output:
            print(f"\n{display.green}Metadata successfully cleared from {image_path}!")
        else:
            print(f"\n{display.red}[!] Error clearing metadata.")

    else:
        print(f"\n{display.red}[!] Invalid file format.")

    input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")


def save_message(image_path, message):
    if not os.path.isfile(image_path):
        print(f"\n{display.red}[!] The provided path is not a valid file.")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
        return

    if not image_path.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        print(f"\n{display.red}[!] Unsupported file format.")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
        return

    try:
        if image_path.endswith(".png"):
            img = Image.open(image_path)
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("Hidden Message", message)
            img.save(image_path, pnginfo=metadata)
        elif image_path.endswith((".jpg", ".jpeg")):
            exif_dict = {"0th": {piexif.ImageIFD.Software: message}}
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, image_path)
        elif image_path.endswith(".webp"):
            img = Image.open(image_path)
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("Hidden Message", message)
            img.save(image_path, "WEBP", pnginfo=metadata)

        print(f'\n{display.green}Message successfully saved to {image_path}!')
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
    except Exception as e:
        print(f"\n{display.red}[!] An error occurred (report this error to the creator): {e}")
        input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")

VERSION = "1.0.0"
