import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default
intents.message_content = True
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix = '!', intents=discord.Intents.default())  # sets up the command prefix

@client.event
async def on_ready():
    print('bot is now online')
    print('-----------------------------------------')

@client.command
async def hello(ctx):  # returns a message when a user type '!hello' in chat
    await ctx.send('Hello there!')

# client.run(bot api address)
