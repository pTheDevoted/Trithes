import os
import sys
import display as display
from pystyle import Colorate, Colors
from rich.console import Console
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from rich.style import Style
import utils

console = Console()

# Estilos para InquirerPy
question_style = Style(color="yellow", bold=True)
choice_style = Style(color="yellow")
pointer_style = Style(color="yellow")
selected_style = Style(color="yellow", bold=True)

# Perguntas para o prompt
questions = [
    {
        "type": "list",
        "name": "choice",
        "message": ("               What do you want?"),
        "choices": [
            "             1. Hide message in an image",
            "             2. Scan image",
            "             3. Exit",
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
        respost = answers['choice']

        if "1" in respost:
            os.system('clear')
            print(Colorate.Horizontal(Colors.yellow_to_red, display.logo))
            image_path = input(f"\n{display.bwhite}[{display.byellow}>{display.bwhite}]{display.white} Enter the path to the image: ")
            message_to_hide = input(f"{display.bwhite}[{display.byellow}>{display.bwhite}]{display.white} Enter the message to be hidden in the image: ")
            if utils.hide_message(image_path, message_to_hide):
                print(f"\n{display.green}Message successfully hidden in {image_path} !{display.white}")
                input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
        elif "2" in respost:
            os.system('clear')
            print(Colorate.Horizontal(Colors.yellow_to_red, display.logo))
            image_path = input(f"\n{display.bwhite}[{display.byellow}>{display.bwhite}]{display.white} Enter the path of the image with the hidden message: ")
            message_recovered = utils.scan_image_metadata(image_path)
            if message_recovered:
                print(f'\n{message_recovered}')
                input(f"\n{display.white}Press {display.bwhite}[ENTER]{display.white} to continue")
        elif "3" in respost:
            os.system('clear')
            print(Colorate.Horizontal(Colors.yellow_to_red, display.banner3))
            print(f"\n{display.byellow}Until next time.")
            sys.exit()
except KeyboardInterrupt:
    print('\n[#] Program interrupted')
