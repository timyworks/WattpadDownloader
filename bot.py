import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.command()
async def download(ctx, url):
    # Add your Wattpad download logic here
    await ctx.send("Downloading from Wattpad... (placeholder)")

bot.run(os.getenv("DISCORD_TOKEN"))
