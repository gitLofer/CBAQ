import user_storage as us
import funkcije as f

import os
import discord # pip install discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

waqiToken = "e95e9dd0a620f4d84415424d036fc493e4059e45"

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
prefix = '?'
bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), intents=intents, help_command=None)

users = us.load_users()

@bot.event
async def on_ready():
    print(users)
    print('Connected to Discord!')

@bot.command(name='help')
# @commands.has_role('Admin')
async def help(ctx):
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    embed = discord.Embed(title="Chatbot for Air Quality", color=0x69a758)
    embed.set_author(name="CBAQ - Help", icon_url="https://www.pinclipart.com/picdir/middle/574-5743354_pollution-and-air-quality-circle-clipart.png")

    help_en = 'Show this message'
    lang_help_en = 'Change language of the bot. Available options are Serbian (RS) and English (EN)'
    uvi_help_en = 'Show the UV index for a given city'
    uvi_forecast_help_en = 'Show a 3-day UV index forecast for a given city'
    aqi_help_en = 'Show the air quality index for a given city'
    geo_help_en = 'Show the geographical coordinates for a given city'

    help_rs = 'Prikazi ovu poruku'
    lang_help_rs = 'Menja jezik bota u željeni. Dostupne opcije su Srpski (RS) i Engleski (EN)'
    uvi_help_rs = 'Prikazuje UV indeks sa uneti grad'
    uvi_forecast_help_rs = 'Prikazuje prognozu 3 dana UV indeksa sa uneti grad'
    aqi_help_rs = 'Prikazuje indeks kvaliteta vazduha za uneti grad'
    geo_help_rs = 'Prikazuje geografske koordinate unetog grada'

    if (lang == 'EN'):
        embed.add_field(name="help", value=help_en, inline=False)
        embed.add_field(name="lang", value=lang_help_en, inline=False)
        embed.add_field(name="uvi", value=uvi_help_en, inline=False)
        embed.add_field(name="uvi-forecast", value=uvi_forecast_help_en, inline=False)
        embed.add_field(name="aqi", value=aqi_help_en, inline=False)
        embed.add_field(name="geo", value=geo_help_en, inline=False)
        try:
            await ctx.message.author.send(embed=embed)
            await ctx.send("Check your DMs!")
            return
        except:
            await ctx.send("Your DMs are disabled, please turn them on so you can receive the help menu!")
    elif (lang == 'RS'):
        embed.add_field(name="help", value=help_rs, inline=False)
        embed.add_field(name="lang", value=lang_help_rs, inline=False)
        embed.add_field(name="uvi", value=uvi_help_rs, inline=False)
        embed.add_field(name="uvi-forecast", value=uvi_forecast_help_rs, inline=False)
        embed.add_field(name="aqi", value=aqi_help_rs, inline=False)
        embed.add_field(name="geo", value=geo_help_rs, inline=False)
        try:
            await ctx.message.author.send(embed=embed)
            await ctx.send("Poslao sam vam poruku!")
            return
        except:
            await ctx.send("Vase privatne poruke su iskljucene. Molim vas da ih uklucite kako bi ste dobili help meni!")


@bot.command(name='aqi', help='Prikazi AQI za neki grad / Show the AQI for a given city')
async def aqi(ctx, *arg1):
    arg1 = ' '.join(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.aqi(arg1.title(), lang)
    await ctx.send(answ)

@bot.command(name='uvi')
async def uvi(ctx, *arg1):
    arg1 = ' '.join(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.uviTrenutno(arg1.title(), lang)
    answ = ''.join(answ)
    await ctx.send(answ)

@bot.command(name='uvi-forecast')
async def uvi_forecast(ctx, *arg1):
    arg1 = ' '.join(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.uviZaNarednaTriDana(arg1, lang)
    await ctx.send(''.join(answ))

@bot.command(name='geo')
async def geo(ctx, *arg1):
    arg1 = ' '.join(arg1)
    # DEBUG: print(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.geo(arg1.title(), lang)
    await ctx.send(''.join(answ))

@bot.command(name='weather')
async def weather(ctx, *arg1):
    arg1 = ' '.join(arg1)
    # DEBUG: print(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.weather(arg1.title(), lang)
    await ctx.send(''.join(answ))

@bot.command(name='lang', help='For English: EN, ENGLISH, ENGLESKI\nZa srpski: RS, SR, SERBIAN, SRPSKI')
async def lang(ctx, arg1):
    arg1 = arg1.upper()
    user_id = ctx.author.id
    if arg1 == 'RS' or arg1 == 'SRPSKI' or arg1 == 'SERBIAN' or arg1 == 'SR':
        us.remove_user_id(user_id, users)
        await ctx.send("Jezik namesten na srpski.")
        return
    elif arg1 == 'EN' or arg1 == 'ENGLESKI' or arg1 == 'ENGLISH':
        us.add_user_id(user_id, users)
        await ctx.send("Language changed to English.")
        return
    await ctx.send("Uneli ste nevazecu opciju. Uradite \"" + prefix + "help lang\" da saznate vise.\nYou've entered an invalid option. Do \"" + prefix + "help lang\" to see all valid options")

# Alijasi za komande
# bot.command(name="weather", pass_context=True)(aqi.callback)

bot.run(TOKEN)
