import json
import discord
from discord.ext import commands
from discord import SlashCommand

f = open("./dao/config.json")
data = json.load(f)

TOKEN = data["Discord"]["Token"]
BOTURL = data["Discord"]["BotURL"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print(f'We have logged in as {client.user}')

async def status_task():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"help"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/invite'):
        await message.channel.send('Hier bekommst du mein Einladungslink: '+ BOTURL)
        

client.run(TOKEN)