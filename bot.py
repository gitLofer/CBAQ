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

try:
    users = us.load_users()
except:
    users = []

@bot.event
async def on_ready():
    print(users)
    print('Connected to Discord!')

@bot.command(name='dm')
async def dm(ctx, *arg1):
    arg1 = ' '.join(arg1)
    channel = bot.get_channel(831843361311948800)
    await channel.send(arg1)

@bot.command(name='help')
# @commands.has_role('Admin')
async def help(ctx):
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    embed = discord.Embed(title="Chatbot for Air Quality", color=0x69a758)
    embed.set_author(name="CBAQ - Help", icon_url="https://www.pinclipart.com/picdir/middle/574-5743354_pollution-and-air-quality-circle-clipart.png")
    vreme = f.vremeTrenutno()
    embed.set_footer(text=vreme[0] + ", " + vreme[1])

    help_en = 'Show this message'
    lang_help_en = 'Change language of the bot. Available options are Serbian (RS) and English (EN)'
    uvi_help_en = 'Show the UV index for a given city'
    uvi_forecast_help_en = 'Show a 3-day UV index forecast for a given city'
    aqi_help_en = 'Show the air quality index for a given city'
    geo_help_en = 'Show the geographical coordinates for a given city'
    weather_help_en = 'Show the weather and temperature for a given city'
    weather_forecast_help_en = 'Show current weather and the projected weather for the next 3 days'

    help_rs = 'Prikaži ovu poruku'
    lang_help_rs = 'Menja jezik bota u željeni. Dostupne opcije su Srpski (RS) i Engleski (EN)'
    uvi_help_rs = 'Prikazuje UV indeks za uneti grad'
    uvi_forecast_help_rs = 'Prikazuje prognozu 3 dana UV indeksa za uneti grad'
    aqi_help_rs = 'Prikazuje indeks kvaliteta vazduha za uneti grad'
    geo_help_rs = 'Prikazuje geografske koordinate unetog grada'
    weather_help_rs = '*Prikazuje vreme i temperaturu za uneti grad'
    weather_forecast_help_rs = 'Prikazuje trenutno vreme i projektovano vreme za naredna 3 dana'

    if (lang == 'EN'):
        embed.add_field(name=":mechanic: help", value=help_en, inline=False)
        embed.add_field(name=":book: lang", value=lang_help_en, inline=False)
        embed.add_field(name=":sunny: uvi", value=uvi_help_en, inline=False)
        embed.add_field(name=":sunny: uvi-forecast", value=uvi_forecast_help_en, inline=False)
        embed.add_field(name=":dash: aqi", value=aqi_help_en, inline=False)
        embed.add_field(name=":earth_africa: geo", value=geo_help_en, inline=False)
        embed.add_field(name=":white_sun_rain_cloud: weather", value=weather_help_en, inline=False)
        embed.add_field(name=":white_sun_rain_cloud: weather-forecast", value=weather_forecast_help_en, inline=False)
        try:
            await ctx.message.author.send(embed=embed)
            await ctx.send("Check your DMs!")
            return
        except:
            await ctx.send("Your DMs are disabled, please turn them on so you can receive the help menu!")
    elif (lang == 'RS'):
        embed.add_field(name=":mechanic: help", value=help_rs, inline=False)
        embed.add_field(name=":book: **lang**", value=lang_help_rs, inline=False)
        embed.add_field(name=":sunny: uvi", value=uvi_help_rs, inline=False)
        embed.add_field(name=":sunny: uvi-forecast", value=uvi_forecast_help_rs, inline=False)
        embed.add_field(name=":dash: aqi", value=aqi_help_rs, inline=False)
        embed.add_field(name=":earth_africa: geo", value=geo_help_rs, inline=False)
        embed.add_field(name=":white_sun_rain_cloud: weather", value=weather_help_rs, inline=False)
        embed.add_field(name=":white_sun_rain_cloud: weather-forecast", value=weather_forecast_help_rs, inline=False)
        try:
            await ctx.message.author.send(embed=embed)
            await ctx.send("Poslao sam vam poruku!")
            return
        except:
            await ctx.send("Vaše privatne poruke su isključene. Molim vas da ih uključite kako bi ste dobili help meni!")


@bot.command(name='aqi')
async def aqi(ctx, *arg1):
    arg1 = ' '.join(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.aqi(arg1.title(), lang)
    await ctx.send(''.join(answ))

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
    if isinstance(answ, discord.Embed):
        await ctx.send(embed=answ)
    else:
        await ctx.send(answ)

@bot.command(name='geo')
async def geo(ctx, *arg1):
    arg1 = ' '.join(arg1)
    # DEBUG: print(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.geo(arg1.title(), lang)
    if isinstance(answ, discord.Embed):
        await ctx.send(embed=answ)
    else:
        await ctx.send(answ)

@bot.command(name='weather')
async def weather(ctx, *arg1):
    arg1 = ' '.join(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.weather(arg1.title(), lang)
    await ctx.send(''.join(answ))

@bot.command(name='weather-forecast')
async def weatherforecast(ctx, *arg1):
    arg1 = ' '.join(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.weatherforecast(arg1, lang)
    if isinstance(answ, discord.Embed):
        await ctx.send(embed=answ)
    else:
        await ctx.send(answ)

@bot.command(name='lang')
async def lang(ctx, arg1):
    arg1 = arg1.upper()
    user_id = ctx.author.id
    if arg1 == 'RS' or arg1 == 'SRPSKI' or arg1 == 'SERBIAN' or arg1 == 'SR':
        us.remove_user_id(user_id, users)
        print(users)
        await ctx.send("Jezik namešten na srpski.")
        return
    elif arg1 == 'EN' or arg1 == 'ENGLESKI' or arg1 == 'ENGLISH':
        us.add_user_id(user_id, users)
        print(users)
        await ctx.send("Language changed to English.")
        return
    await ctx.send("Uneli ste nevažeću opciju. Uradite \"" + prefix + "help lang\" da saznate više.\nYou've entered an invalid option. Do \"" + prefix + "help lang\" to see all valid options")

# Alijasi za komande
bot.command(name="AQI", pass_context=True)(aqi.callback)
bot.command(name="UVI", pass_context=True)(uvi.callback)
bot.command(name="UVI-FORECAST", pass_context=True)(uvi_forecast.callback)
bot.command(name="LANG", pass_context=True)(lang.callback)
bot.command(name="WEATHER", pass_context=True)(weather.callback)
bot.command(name="WEATHER-FORECAST", pass_context=True)(weatherforecast.callback)
bot.command(name="GEO", pass_context=True)(geo.callback)
bot.command(name="HELP", pass_context=True)(help.callback)

bot.run(TOKEN)
