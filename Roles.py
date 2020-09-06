import discord
import sys
import subprocess 
from subprocess import call
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")

@bot.command()
@commands.has_role('ayylmao')
async def ayy(ctx, arg):
    await ctx.send("Please Wait...")
    text_file = open("URL.txt", "a")  
    text_file.write(arg+"\n")
    await ctx.send(arg + " was added!")


@bot.command()
@commands.has_role('ayylmao')
async def go(ctx):
    await ctx.send("Loading...")
    subprocess.call("YT.py", shell=True)
    await ctx.send("Downloaded!")

@bot.command()
@commands.has_role('ayylmao')
async def send(ctx):
    await ctx.send("Sending...")
    await ctx.message.channel.send(file=discord.File(' 1.mp3'))
    await ctx.send("Sent!")

@bot.command()
@commands.has_role('ayylmao')
async def gone(ctx):
    await ctx.send("Deleted...")
    subprocess.call("DEL.py", shell=True)
bot.run('TOKEN')
