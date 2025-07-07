import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix = '!', intents=intents)  # sets up the command prefix

@bot.event
async def on_ready():
    print(f'bot is now online, bot {bot.user.name}')
    print('-----------------------------------------')

@bot.event
async def on_member_join(member):
    await member.send(f'{member.name}, bingus greets you.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "hippo" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} bingus does not like hippos")

    await bot.process_commands(message)  # this needs to be here at the end for message functions

@bot.command
async def hello(ctx):  # returns a message when a user type '!hello' in chat
    await ctx.send('Hello there!')

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
# client.run(bot api address)
