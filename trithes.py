import os
import sys
import argparse
import display as display
from pystyle import Colorate, Colors
from rich.console import Console
from InquirerPy import prompt
from rich.style import Style
import utils

console = Console()

# modo de argumeto

def run_argument_mode():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-s", "--scan", help="Path to file to scan or embed message")
    parser.add_argument("-m", "--message", help="Message to hide (used with -s)")
    parser.add_argument("-h", "--help", action="store_true", help="Show help and valid formats")
    args = parser.parse_args()

    if args.help:
        print(Colorate.Horizontal(Colors.red_to_yellow, display.logo))
        print(f"""{display.byellow}
Usage:
  python trithes.py -s <file>               Scan metadata
  python trithes.py -s <file> -m <message>  Hide message in file (steganography)
  python trithes.py -h                      Show this help and info

Supported formats for scan (via ExifTool): JPG, JPEG, PNG, PDF, WEBP, MP4, MP3, DOCX, XLSX, PPTX, JSON, ZIP, and 100+ others.
Steganography supports: JPG, PNG, WEBP, PDF

Project: https://github.com/pTheDevoted
        """)
        return

    if args.scan and args.message:
        if os.path.isfile(args.scan):
            if utils.hide_message(args.scan, args.message):
                print(f"\n{display.green}Message successfully hidden in {args.scan}")
        else:
            print(f"{display.red}[!] File not found: {args.scan}")
        return

    elif args.scan:
        if os.path.isfile(args.scan):
            utils.scan_image_metadata(args.scan)
        else:
            print(f"{display.red}[!] File not found: {args.scan}")
        return

    # Se nenhum dos padrões for atendido:
    print("[!] Invalid or missing arguments.")
    print("Use 'python trithes.py -h' for help or run without arguments to use the menu.")


# modo de menu

def run_menu_mode():
    question_style = Style(color="yellow", bold=True)

    questions = [
        {
            "type": "list",
            "name": "choice",
            "message": ("               What do you want?"),
            "choices": [
                "             1. Hide message (JPG, PDF, PNG, WEBP)",
                "             2. Scan file metadata (130+ formats)",
                "             3. Info",
                "             4. Exit",
            ],
        }
    ]

    try:
        while True:
            os.system('clear')
            print(Colorate.Horizontal(Colors.yellow_to_red, display.logo))
            print(f" {display.lwhite}v{utils.VERSION}{' ' * 17}https://github.com/pTheDevoted\n")

            answers = prompt(questions, style={
                "question": "fg:ansiyellow bold",
                "pointer": "fg:ansiyellow",
                "highlight": "fg:ansired bold",
                "answer": "fg:ansiyellow bold",
            })
            respost = answers['choice'].strip()

            if respost.startswith("1."):
                os.system('clear')
                print(Colorate.Horizontal(Colors.yellow_to_red, display.logo))
                file_path = input(f"\n{display.bwhite}[{display.byellow}>{display.bwhite}]{display.white} Enter the path to the file: ")
                message_to_hide = input(f"{display.bwhite}[{display.byellow}>{display.bwhite}]{display.white} Enter the message to be hidden: ")
                if utils.hide_message(file_path, message_to_hide):
                    print(f"\n{display.green}Message successfully hidden in {file_path} !{display.white}")
                    input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")

            elif respost.startswith("2."):
                os.system('clear')
                print(Colorate.Horizontal(Colors.yellow_to_red, display.logo))
                file_path = input(f"\n{display.bwhite}[{display.byellow}>{display.bwhite}]{display.white} Enter the path of the file to scan: ")
                utils.scan_image_metadata(file_path)

            elif respost.startswith("3."):
                os.system('clear')
                print(Colorate.Horizontal(Colors.yellow_to_red, display.logo))
                print(f"\n{display.byellow}This tool was made for metadata testing and steganography research.\nCheck out the project: https://github.com/pTheDevoted")
                input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to return to menu")

            elif respost.startswith("4."):
                os.system('clear')
                print(Colorate.Horizontal(Colors.yellow_to_red, display.banner3))
                print(f"\n{display.byellow}Until next time.")
                sys.exit()

    except KeyboardInterrupt:
        print('\n[#] Program interrupted')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_argument_mode()
    else:
        run_menu_mode()
