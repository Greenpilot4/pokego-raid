from os import system
import platform
from discord.ext import commands
from colorama import Fore, init
from bs4 import BeautifulSoup
import requests
import json
import time

init()

# Old Code if you read this please give feedback, maybe I should use 2d arrays instead of 2?

try:
    with open('token.json') as f:
        data = json.load(f)
    if data['token'] == "":
        token = input("[-] Token: ")
    else:
        token = data['token']
except FileNotFoundError:
    token = input("[-] Token: ")
    tokendata = {"token": token}
    with open('token.json', 'w') as outfile:
        json.dump(tokendata, outfile)


r = requests.get("https://thesilphroad.com/raid-bosses")
soup = BeautifulSoup(r.text, "html.parser")

real_list = []
display_list = []
for pokemon in soup.find_all("div", class_="boss-name"):
    pocket_monster = pokemon.get_text()

    if "mega" in pocket_monster.lower():

        full_pokemon = pocket_monster.split(" ")
        mega = full_pokemon[0]
        pokemon = full_pokemon[1] + "-"

        if " y" in pocket_monster.lower() or " x" in pocket_monster.lower():
            extension = full_pokemon[2] + "-"

            real_list.append(pokemon + extension + mega)

        else:
            real_list.append(pokemon + mega)

    elif "shadow" in pocket_monster.lower():
        full_pokemon = pocket_monster.split(" ")
        shadow = full_pokemon[0]
        pokemon = full_pokemon[1] + "-"

        real_list.append(pokemon + shadow)

    elif "alolan" in pocket_monster.lower():
        full_pokemon = pocket_monster.split(" ")
        alolan = full_pokemon[0]
        pokemon = full_pokemon[1] + "-"

        real_list.append(pokemon + alolan)

    elif "flying" in pocket_monster.lower():
        full_pokemon = pocket_monster.split(" ")
        flying = full_pokemon[0]
        pokemon = full_pokemon[1] + "-"

        real_list.append(pokemon + flying)

    else:
        real_list.append(pocket_monster)

    display_list.append(pocket_monster)


bot = commands.Bot(command_prefix="!pokegoRR!", self_bot=True)
pokeNav = 428187007965986826

if platform.system() == "Windows":
    system("cls")
else:
    system("clear")

print(Fore.LIGHTRED_EX + """\

██████╗  ██████╗ ██╗  ██╗███████╗ ██████╗  ██████╗     ██████╗  █████╗ ██╗██████╗ 
██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔════╝ ██╔═══██╗    ██╔══██╗██╔══██╗██║██╔══██╗
██████╔╝██║   ██║█████╔╝ █████╗  ██║  ███╗██║   ██║    ██████╔╝███████║██║██║  ██║
██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║   ██║██║   ██║    ██╔══██╗██╔══██║██║██║  ██║
██║     ╚██████╔╝██║  ██╗███████╗╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║██║██████╔╝
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ 
 """ + Fore.RESET)

pokemon_counter = 1
for pocket_monster in display_list:
    print(Fore.LIGHTBLUE_EX + str(pokemon_counter) + ". " + Fore.LIGHTMAGENTA_EX + pocket_monster + Fore.RESET)
    pokemon_counter += 1

print(Fore.LIGHTBLUE_EX + str(pokemon_counter) + ". " + Fore.LIGHTMAGENTA_EX + "List custom pokemon:")
pokemonIN = input(Fore.YELLOW + "\n[-] Select a Number: " + Fore.RESET)
try:
    pokeOption = int(pokemonIN)
except ValueError:
    print(Fore.LIGHTRED_EX + "[+] Please enter a valid number!")
    pokeOption = 0

if pokeOption == pokemon_counter:
    plist = input(Fore.YELLOW + "[-] List custom pokemon: " + Fore.RESET)
    pokemon = plist.split()
elif pokeOption <= 0 or pokeOption > len(real_list):
    print(Fore.LIGHTRED_EX + "[+] Not a valid option!")
else:
    pokemon = real_list[pokeOption - 1]


@bot.event
async def on_reaction_add(reaction, user):
    current_time = time.strftime("%H:%M:%S ", time.localtime())
    start_time = time.time()

    if user.id == pokeNav and reaction.emoji == "🧧" and any(
            word in reaction.message.content.lower() for word in pokemon):
        try:
            await reaction.message.add_reaction("🧧")
            delay = (time.time() - start_time)
            print(Fore.LIGHTCYAN_EX + current_time + Fore.YELLOW + "[+] Joined a", pokemon + Fore.RESET)
            print(" Delay:" + Fore.GREEN + " %.3fs" % delay + Fore.RESET)

            end_input = input(Fore.YELLOW + "[+] Press enter to end: ")
            exit()

        except:
            print(Fore.LIGHTCYAN_EX + current_time + Fore.LIGHTRED_EX + "[+] Something went wrong trying again..")
            pass


bot.run(token, bot=False)
