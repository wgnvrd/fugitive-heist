import os
import discord
import json
from game_api import GameAPI

client = discord.Client(intents=discord.Intents.all())
channel = 0
specific_message = 0
global gamee
gamee = GameAPI()

@client.event
async def on_ready():
    print("Online")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content == "ping":
            await message.channel.send("pong")
        if message.content == "Start!":
            if gamee.getStatus != "Running":
                specific_message = await message.channel.send("```React here to join a team \n 🔴 Fugitives \n 🔵 Guards```")
                await specific_message.add_reaction('🔴')
                await specific_message.add_reaction('🔵')
                gamee.set_game_leader(message.author.id)
                gamee.start()
                

@client.event
async def on_reaction_add(reaction, user):
    Channel = client.get_channel(1083072190515265736)
    if reaction.message.channel.id != Channel.id: #Makes sure its only this random channel
        return
    if user.id == 1080335845694902302: #this is the bot's ID. Can't have it looking at its own message can we?
        return
    FugRole = discord.utils.get(user.guild.roles, name="Fugitives")
    GuardRole = discord.utils.get(user.guild.roles, name="Guards")
    if reaction.emoji == "🔴":
        if GuardRole in user.roles:
            await user.remove_roles(GuardRole)
        await user.add_roles(FugRole)
        if 
    elif reaction.emoji == "🔵":
        if FugRole in user.roles:
            await user.remove_roles(FugRole)
        await user.add_roles(GuardRole)

# check if environment variable (production)
if 'FH_BOT_TOKEN' in os.environ:
    bot_token = os.environ['FH_BOT_TOKEN']
else:
    with open('config.json') as f:
        config = json.load(f)
        bot_token = config['BOT_TOKEN']
    
client.run(bot_token)