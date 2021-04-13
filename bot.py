import os
import discord # pip install discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print('Connected to Discord!')

bot.run(TOKEN)

















