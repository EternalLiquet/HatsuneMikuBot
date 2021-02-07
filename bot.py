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

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

@bot.event
async def on_message(message):
    if 'all in?' in message.content:
        channel = message.channel
        await channel.send("Tesla!")
    elif 'Tesla!' in message.content:
        channel = message.channel
        await channel.send("all in?")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')



bot.run(TOKEN)
