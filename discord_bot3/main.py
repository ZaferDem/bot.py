import os
from dotenv import load_dotenv
load_dotenv()

TOKEN =os.environ.get("DISCORD_BOT")

import discord
from discord.ext import commands

izinler = discord.Intents.all()
izinler.message_content =True

piton = commands.Bot(command_prefix="/", intents=izinler)

@piton.event
async def on_read():
    print(f"{piton.user.name} is ready")

@piton.command()
async def merhaba(ctx):
    await ctx.send("Merhaba!")

@piton.command()
async def naber(ctx):
    await ctx.send("İyidir Senden?")

#@piton.command()
#async def add( )
#    await ct

piton.run(TOKEN)
