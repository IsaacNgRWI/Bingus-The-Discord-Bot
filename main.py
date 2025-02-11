import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!', intents=discord.Intents.default())  # sets up the command prefix

@client.event
async def on_ready():
    print('bot is now online')
    print('-----------------------------------------')

@client.command
async def hello(ctx):  # returns a message when a user type '!hello' in chat
    await ctx.send('Hello there!')

# client.run(bot api address)
