import requests
import pyperclip

logo = '''
████████╗░█████╗░██████╗░██████╗░███████╗███╗░░██╗████████╗  ░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗░██║╚══██╔══╝  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
░░░██║░░░██║░░██║██████╔╝██████╔╝█████╗░░██╔██╗██║░░░██║░░░  ╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
░░░██║░░░██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║╚████║░░░██║░░░  ░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
░░░██║░░░╚█████╔╝██║░░██║██║░░██║███████╗██║░╚███║░░░██║░░░  ██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝'''
print(logo)
print(" ")
print(" Credit : * Utkarsh Kanojiya \n          * CyberBoySumanjay")
print("\n")
movie_name = input("Enter Movie Name :-- ")
url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"
torrent_result = requests.get(url).json()

index = 1
magnet = []
for result in torrent_result:
    if 'movie' in result['type'].lower():
        print(index, ")", result['name'], "-->>", result['size'])
        index = index + 1
        magnet.append(result['magnet'])

choice = int(input("Enter Number Which Torrent You Want -> "))
print(" ")
print("Magnet Link Of Your File ", magnet[choice - 1])
pyperclip.copy(magnet[choice - 1])
print(" ")
print("Your Magnet Link Copied On Clipboard")
