import os
import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

def list_directory_structure(directory_path, indent=""):
    try:
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)

            if os.path.isdir(item_path):
                print(Fore.BLUE + indent + f"📁 {item}")
                list_directory_structure(item_path, indent + "  ") 
            else:
                print(Fore.GREEN + indent + f"📄 {item}")

    except FileNotFoundError:
        print(Fore.RED + "Директорія не існує.")

direct = list_directory_structure("D:\Python\__pycache__\laboratory")
print(direct)