<<<<<<< HEAD
<<<<<<< HEAD
import asyncio
import os
import random
import discord
from discord.ext import commands,tasks
from datetime import datetime

token = ''

intents = discord.Intents.all()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)

#guildid = guild.id for guild in bot.guilds
log_channel_id = 1348018366996287528
bot_channel_id = 1347722353068740650
raidhelperid = 579155972115660803

msgl = list()
#guild = client.get_guild(guildid)



@client.event
async def on_ready():
    for guild in bot.guilds:
        log_channel = discord.utils.get(guild.text_channels, id=log_channel_id)
        bot_channel = discord.utils.get(guild.text_channels, id=bot_channel_id)
        print('ginger',raidhelperid,log_channel,bot_channel)
#    for msg in bot_channel.history(limit=5).flatten():
#        if msg.author == raidhelperid:
#            print(f'Message: {msg.content} - Time: {msg.created_at}')
#            msgl.append(msg)
    return

@client.event
async def on_raw_message_edit(payload):
    after = payload.message.content
    if before:
        for msg in msgl:
            if msg.id == payload.id:
                before = msg.content
    if before != after:
        Lbefore: list[str] = sorted(before)
        Lafter: list[str] = sorted(after)
        if len(Lafter)>len(Lbefore):
            for element in Lbefore:
                Lafter.remove(element)
                print(Lafter + "Signed up at" + datetime)
        else:
            for element in Lafter:
                Lbefore.remove(element)
                print(Lbefore + "Bailed on us niggas at" + datetime)
        before = after



    print(payload, 'and')
    print(payload.message.content)
    print('''



    ''')




bot.run(token)
            
                



        

=======
print("whats up tos")
>>>>>>> parent of 94d5233 (summary required)
=======
print("whats up tos")
>>>>>>> parent of 94d5233 (summary required)
