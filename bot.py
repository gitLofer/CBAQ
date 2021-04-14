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

@bot.command(name='dm')
# @commands.has_role('Admin')
async def dm(ctx):
    await ctx.message.author.send("U buducnosti ce ovako da salje help")

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
async def uvi(ctx, *arg1):
    arg1 = ' '.join(arg1)
    # DEBUG: print(arg1)
    user_id = ctx.message.author.id
    lang = us.user_lang(user_id, users)
    answ = f.geo(arg1.title(), lang)
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
