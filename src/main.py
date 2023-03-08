import os
import discord
import json

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

# check if environment variable (production)
if 'FH_BOT_TOKEN' in os.environ:
    bot_token = os.environ['FH_BOT_TOKEN']
else:
    # if not, read from config.json
    with open('config.json') as f:
        config = json.load(f)
        bot_token = config['BOT_TOKEN']
    
client.run(bot_token)