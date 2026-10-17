import pyfiglet
from colorama import Fore, Style, init  


init(autoreset=True)

text = input("Enter the text: ")
art = pyfiglet.figlet_format(text)

print(Fore.BLUE + art)