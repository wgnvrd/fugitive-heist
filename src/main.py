import os
import discord

discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Online")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content == "ping":
            await message.channel.send("pong")

my_secret = os.environ['BOT_TOKEN']
client.run(my_secret)