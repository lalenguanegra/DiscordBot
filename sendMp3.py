@bot.command()
async def send(ctx):
    await ctx.send("Sending...")
    area=ctx.message.channel
    await channel.send(area, file=discord.File(' 1.mp3'))
    await ctx.send("Sent!")
