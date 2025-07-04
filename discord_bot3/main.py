import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ.get("DISCORD_BOT")

import discord
from discord.ext import commands

izinler = discord.Intents.all()
izinler.message_content = True
izinler.members = True

piton = commands.Bot(command_prefix="/", intents=izinler)

@piton.event
async def on_ready():
    print(f"{piton.user.name} is ready")

@piton.event
async def on_message(msg):
    if msg.author.bot:
        return
    if "http" in msg.content:
        await msg.delete()
        await msg.guild.ban(msg.author, reason="Reklam")

@piton.event
async def on_member_join(member):
    # Karşılama mesajı gönderme
    for channel in member.guild.text_channels:
        await channel.send(f" Hoş geldiniz: , {member.mention}!")



@piton.command()
async def merhaba(ctx):
    await ctx.send("Merhaba!")

@piton.command()
async def naber(ctx):
    await ctx.send("İyidir Senden?")

@piton.command()
async def add(ctx, a: float, b: float):
    await ctx.send(f"{a} + {b} = {a + b}")

@piton.command("at")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    if member:
        if ctx.author.top_role <= member.top_role:
            await ctx.send("senden büyüğü atamazsın")
        else:
            await ctx.guild.ban(member)
            await ctx.send(f"{member.name} atıldı")
    else:
        await ctx.send("atmak istediğiniz kullanıcıyı belirtin")

piton.run(TOKEN)
