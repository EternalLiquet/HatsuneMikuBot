import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime
load_dotenv()

bot = commands.Bot(command_prefix='>')
client = discord.Client()


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@client.event
async def on_message(message):
    moment = datetime.datetime.now()
    if moment.hour >= 2 or moment.hour <= 5:
        await message.channel.send('It\'s time for beddy byes, {}, you need your beauty sleep <3. \nhttps://i.pinimg.com/originals/de/f3/2b/def32b29236bebf71e878e4bab16f278.jpg'.format(message.author.name))

TOKEN = os.getenv('token')

bot.run(TOKEN)
