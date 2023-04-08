import os
import discord
import json
from game_api import GameAPI
import asyncio
from qr_reader import read_qr

client = discord.Client(intents=discord.Intents.all())
channel = 0
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
                global specific_message
                specific_message = await message.channel.send("```React here to join a team \n 🔴 Fugitives \n 🔵 Guards```")
                await specific_message.add_reaction('🔴')
                await specific_message.add_reaction('🔵')
                gamee.set_game_leader(message.author.id)
                gamee.setStatus("Running")

        if message.author.id == gamee.get_game_leader():
            if message.content == "Continue!":
                if gamee.getStatus != "Playing":
                    await specific_message.clear_reaction('🔵')
                    await specific_message.clear_reaction('🔴')
                    await message.channel.send("```Game Start```")
                    gamee.setStatus("Playing")

                    time = 10
                    timeMessage = await message.channel.send("00:00")
                    await timer(time, timeMessage)
                    await message.channel.send("```Game End```")
                    gamee.setStatus("Off")
        if message.attachments:
            roles = [role.name for role in message.author.roles]
            cdn_url = message.attachments[0].url
            if "Fugitives" in roles:
                # Process QR code here
                await message.channel.send("Processing QR code...")
                await message.channel.send(cdn_url)
                data = read_qr(url=cdn_url)
                if data:
                    await message.channel.send(data)
                else:
                    await message.channel.send("No QR code found.")
            elif "Guards" in roles:
                # Tag here
                pass
            else:
                pass

def scan_qr_code(cdn_url):
    pass

def tag_player():
    pass

@client.event
async def on_reaction_add(reaction, user):
    # Channel = client.get_channel(1080336017405517857)
    # if reaction.message.channel.id != Channel.id: #Makes sure its only this random channel
    #     return
    if user.id == 1080335845694902302: #this is the bot's ID. Can't have it looking at its own message can we?
        return
    status = gamee.getStatus()
    if status == "Running":
        FugRole = discord.utils.get(user.guild.roles, name="Fugitives")
        GuardRole = discord.utils.get(user.guild.roles, name="Guards")
        if reaction.emoji == "🔴":
            if GuardRole in user.roles:
                await user.remove_roles(GuardRole)
            await user.add_roles(FugRole)
        elif reaction.emoji == "🔵":
            if FugRole in user.roles:
                await user.remove_roles(FugRole)
            await user.add_roles(GuardRole)

async def timer(time, timerMessage):
    currenttime = time
    while currenttime > -1:
        await asyncio.sleep(1)
        minutes = str(currenttime // 60)
        seconds = str(currenttime % 60)
        await timerMessage.edit(content=minutes.zfill(2) + ":" + seconds.zfill(2))
        currenttime -= 1



# check if environment variable (production)
if 'FH_BOT_TOKEN' in os.environ:
    bot_token = os.environ['FH_BOT_TOKEN']
else:
    with open('config.json') as f:
        config = json.load(f)
        bot_token = config['BOT_TOKEN']
    
client.run(bot_token)