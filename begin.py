# For Windows 10 CMD (Command Prompt) USE 
# RUN begin.bat
import discord
import sys
import subprocess 
from subprocess import call
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

@bot.command()
async def ayy(ctx, arg):
    await ctx.send("Please Wait...")
    text_file = open("URL.txt", "a")  
    text_file.write(arg+"\n")
    await ctx.send(arg + " was added!")


@bot.command()
async def go(ctx):
    await ctx.send("Loading...")
    subprocess.call("YT.py", shell=True)
    await ctx.send("downloaded!")
bot.run('token')









