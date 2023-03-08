import os
import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Online")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content == "ping":
            await message.channel.send("pong")

bot_token = os.environ['FH_BOT_TOKEN']
client.run(bot_token)