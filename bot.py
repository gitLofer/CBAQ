import requests
import json

import user_storage as us

import os
import discord # pip install discord
from discord.ext import commands
from dotenv import load_dotenv


def get_json_from_api(cityName, APItoken):
    r = "https://api.waqi.info/feed/" + cityName + "/?token=" + APItoken
    return (requests.get(r)).json()

def get_city_info(cityName, lang):
    cityJSON = get_json_from_api(cityName, waqiToken)
    cityName = cityName.title()
    if (cityJSON['status'] == 'ok'):
        if lang == 'RS':
            return "Kvalitet vazduha u gradu " + cityName + " je " + str(cityJSON['data']['aqi'])
        elif lang == 'EN':
            return "Air quality in " + cityName + " is " + str(cityJSON['data']['aqi'])
    else:
        if lang == 'RS':
            return "Uneli ste nevazeci grad!"
        elif lang == 'EN':
            return "The requested city could not be found."

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

waqiToken = "e95e9dd0a620f4d84415424d036fc493e4059e45"

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
prefix = '?'
bot = commands.Bot(command_prefix=prefix, intents=intents)

users = us.load_users()

@bot.event
async def on_ready():
    print(users)
    print('Connected to Discord!')

@bot.command(name='aqi', alias='time', help='Prikazi AQI za neki grad / Show the AQI for a given city')
async def aqi(ctx, arg1):
    print(users)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    print(lang)
    answ = get_city_info(arg1, lang)
    await ctx.send(answ)

@bot.command(name='lang', help='For English: EN, ENGISH, ENGLESKI\nZa srpski: RS, SERBIAN, SRPSKI')
async def lang(ctx, arg1):
    arg1 = arg1.upper()
    user_id = ctx.author.id
    if arg1 == 'RS' or arg1 == 'SRPSKI' or arg1 == 'SERBIAN':
        us.remove_user_id(user_id, users)
        await ctx.send("Jezik namesten na srpski.")
        return
    elif arg1 == 'EN' or arg1 == 'ENGLESKI' or arg1 == 'ENGLISH':
        us.add_user_id(user_id, users)
        await ctx.send("Language changed to English.")
        return
    await ctx.send("Uneli ste nevazecu opciju. Uradite \"" + prefix + "help lang\" da saznate vise.\nYou've entered an invalid option. Do \"" + prefix + "help lang\" to see all valid options")

# Alijasi za komande
bot.command(name="weather", pass_context=True)(aqi.callback)

bot.run(TOKEN)
