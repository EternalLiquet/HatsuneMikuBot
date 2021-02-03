import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
TOKEN = os.getenv('token')

bot.run(TOKEN)