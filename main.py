import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("DS_TOKEN_ID")

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Enable specific intents as needed

# Create bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.load_extension('cogs.create')
    for cog in bot.cogs:
        print(f'- {cog}')


bot.run(key)