import discord
from discord.ext import commands
from model import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for a in ctx.message.attachments:
            file_name = a.filename
            file_url = a.url
           
            await a.save(f"./images/{file_name}")
            await ctx.send (getclass(f"./images/{file_name}"))
    else:
        await ctx.send("image not found!")

bot.run("MTQxOTc4MzkyOTMwNDcxMTI1MA.GR6iOL.AqjM13-PkTvbz9S9wH2XoSPmaqVcufjmrUYMuA")
