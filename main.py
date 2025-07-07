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

test_role = "bingu"

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

@bot.command()  # bot.commands() needs a bracket following it unlike bot.events that dont
async def hellob(ctx):  # ctx means context or the person or event that triggered the command
    await ctx.send(f"{ctx.author.mention} bingus greets you.")  # ctx.send sends the message in the channel it was triggered

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=test_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} you are now a servent of bingus")
    else:
        await ctx.send(f"{ctx.author.mention} {role} role does not exist")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=test_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention}, you are now free of the shackles of bingus")
    else:
        await ctx.send(f"{ctx.author.mention}, you were never granted the role of {role}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)  # needs to be at the end (python sequential processing)
# client.run(bot api address)
