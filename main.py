import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import logging
from asyncio import sleep
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix = '!', intents=intents)  # sets up the command prefix

bingu_role = "bingu"

@bot.event
async def on_ready():
    print(f'bot is now online, bot: {bot.user.name}')
    print(f"Initiation time: {datetime.now( )}")
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

    await bot.process_commands(message)  # this needs to be here at the end for on_message functions

@bot.command()
async def aid(ctx):
    embedded_message = discord.Embed(title="The phrases to reach Bingus are as follows:", description="""!hellob:  You greets bingus warmly and will result in Bingus returning the favor.
    !pledge:  You pledge your allegiance to Bingus, becoming a servant of it, bingu.
    !escape:  You forfeit your privilege to be a servant of Bingus, you are now binguless.
    !verify:  You look up to Bingus for validation and he confirms you a real one.
    !dm:  You send Bingus a message and he replies to you in your dms.
    !reply:  You force Bingus to reply to your message regardless of whether it wants to or not.
    !poll:  You summon Bingus to ascertain the opinion of the masses, collected as cute emojis.""")
    await ctx.send(embed=embedded_message)


@bot.command()  # bot.commands() needs a bracket following it unlike bot.events that dont
async def hellob(ctx):  # ctx means context or the person or event that triggered the command
    await ctx.send(f"{ctx.author.mention} bingus greets you.")  # ctx.send sends the message in the channel it was triggered

@bot.command()
async def pledge(ctx):
    role = discord.utils.get(ctx.guild.roles, name=bingu_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} you are now a servent of bingus")
    else:
        await ctx.send(f"{ctx.author.mention} {role} role does not exist")

@bot.command()
async def escape  (ctx):
    role = discord.utils.get(ctx.guild.roles, name=bingu_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention}, you are now free of the shackles of bingus")
    else:
        await ctx.send(f"{ctx.author.mention}, you were never granted the role of {role}")

@bot.command()
@commands.has_role(bingu_role)
async def verify(ctx):
    await ctx.send(f"{ctx.author.mention}, you are a certified servent of bingus")

@verify.error
async def verify_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"{ctx.author.mention}, you are no true bingu")
    else:
        await ctx.send(f"error: {error}")

@bot.command()
# !dm hello world  # "hello world" would be the msg
async def dm(ctx, *, msg):
    await ctx.author.send(f"tf did you mean by {msg}")

@bot.command()
async def reply(ctx):
    await ctx.reply("type shyt")

@bot.command()
async def poll(ctx, *, question):
    embedded_message = discord.Embed(title="make your opinions known", description=question)
    poll_message = await ctx.send(embed=embedded_message)
    await poll_message.add_reaction("😞")
    await poll_message.add_reaction("👍")

@bot.command(pass_context = True)
async def p (ctx):
    await ctx.send("plankton request received")
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        source = FFmpegPCMAudio('plankton-augh.mp3')
        voice = await channel.connect()
        voice.play(source)
        await sleep(3)
        await ctx.voice_client.disconnect()

    else:
        await ctx.send("You need to be in a voice channel to hear plankton")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)  # needs to be at the end (python sequential processing)
# client.run(bot api address)
