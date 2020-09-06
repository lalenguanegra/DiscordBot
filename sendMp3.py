@bot.command()
async def send(ctx):
    await ctx.send("Sending...")
    await ctx.message.channel.send(file=discord.File(' 1.mp3'))
    await ctx.send("Sent!")
