import discord
from discord.ext import commands
import random

# ------------------------------------- CONSTANTS -------------------------- #
BOT_CREATOR_USERNAME = "phucsetup1@gmail.com"
TOKEN = "MTAxMzc4MDExMTY3MTE3MzEzMA.GjZERM.xBnDKSkR0PBo2hNH1moy7wACC-PX6dG5a0bTaw"
LINK = "https://discord.com/api/oauth2/authorize?client_id=1013780111671173130&permissions=8&scope=bot"


intents = discord.Intents.all()

client = commands.Bot(command_prefix='!!', intents=intents)


@client.event
async def on_ready():
    print(client.user)
    print("The bot is now ready for use!")
    print("-----------------------------")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)
