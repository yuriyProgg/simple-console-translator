import json
import requests
from colorama import Fore
import sys
import os


API = "https://ftapi.pythonanywhere.com/translate"
FILE = f"{os.path.dirname(__file__)}/lang.txt"  # Settings languages


try:
    fromLang, toLang = sys.argv[1].split("-")
except IndexError:
    print(
        "Enter: translate < first language >-< second language >\nExample: translate en-ru\n"
    )
    exit()

if "-h" in sys.argv:
    print(Fore.GREEN + "OPTIONS:" + Fore.RESET)
    print("\n-set: set languages")
    print("-h: show all options")
if "-s" in sys.argv:
    fromLang = input("First language: ")
    toLang = input("Second language: ")


print(
    Fore.BLUE
    + "Translate from "
    + Fore.RED
    + fromLang
    + Fore.BLUE
    + " to "
    + Fore.RED
    + toLang
    + Fore.RESET
)
text = input("Enter text: ")

if not text:
    exit()

response = requests.get(f"{API}?sl={fromLang}&dl={toLang}&text={text}")
data = json.loads(response.text)
response.close()

print(Fore.CYAN + "\nTranslate: " + Fore.RESET + data.get("destination-text", ""))
print(
    Fore.CYAN
    + "Possible translations: "
    + Fore.RESET
    + f" {Fore.RED + "|" + Fore.RESET} ".join(
        data["translations"].get("possible-translations")
    )
)
