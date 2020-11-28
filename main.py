from discord.ext import commands
from colorama import Fore
import json
import time

with open('token.json') as f:
    data = json.load(f)
token = data['token']

print(Fore.RED + """\
                 __                             _     __   
    ____  ____  / /______ _____     _________ _(_)___/ /   
   / __ \/ __ \/ //_/ __ `/ __ \   / ___/ __ `/ / __  /    
  / /_/ / /_/ / ,< / /_/ / /_/ /  / /  / /_/ / / /_/ /     
 / .___/\____/_/|_|\__, /\____/  /_/   \__,_/_/\__,_/      
/_/               /____/                                   
 """ + Fore.RESET)

bot = commands.Bot(command_prefix=".", self_bot=True)
pokeNav = 289916458258006016
pPokemon = [
    "azelf",
    "mespirt",
    "uxie",
    "charizard-mega-x",
    "charizard-mega-y",
    "blastoise-mega",
    "houndoom-mega",
    "beedrill-mega",
    "pidgeot-mega",
    "gengar-mega",
]

print(Fore.YELLOW + """\
1. Azelf                     
2. Mespirt                   
3. Uxie                      
4. Mega Charizard X          
5. Mega Charizard Y          
6. Mega Blastoise            
7. Mega Houndoom             
8. Mega Beedrill             
9. Mega Pidgeot 
10. Mega Gengar 
11. All Pokemon             
""" + Fore.RESET)

pokemonIN = input(Fore.MAGENTA + "Select a Number: " + Fore.RESET)

try:
    pokeOption = int(pokemonIN)
except ValueError:
    print("Please Enter a Number!")
    quit()

if pokeOption <= 10:
    pokemon = pPokemon[pokeOption-1]
elif pokeOption == 0:
    print("Not a valid option!")
else:
    pokemon = pPokemon

@bot.event
async def on_reaction_add(reaction, user):
    if user.id == pokeNav and reaction.emoji == "🧧":
        if any(word in reaction.message.content.lower() for word in pokemon):
            await reaction.message.add_reaction("🧧")
            print("Joined a raid!")

bot.run(token, bot=False)
