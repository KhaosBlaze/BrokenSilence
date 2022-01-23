# bot.py
import os
import discord
import asyncio
import random
from discord.ext import commands
from dotenv import load_dotenv

#Store bot token in local .env file or replace DISCORD_TOKEN
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

#Setup bot
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="&", intents=intents)

#Boolean intended to stop infinite loop of annoy, doesn't work due ot async nature
annoy_boolean = False

# Function utilized to convert time to usable formats for randint
def time_convert(num):
    if(num.endswith('s')):
        time = int(num.rstrip('s'))
        if time < 10:
            return 10
        else:
            return time
    elif(num.endswith('m')):
        return int(num.rstrip('m')) * 60
    elif(num.isdecimal()):
        return int(num)
    elif(num == None):
        return 600
    else:
        return False

#Messaging command, replace author Ids with any user you'd like
@client.command()
async def ping(ctx):
    response = ""
    if ctx.author.id == 374398218886447108:
        response = "Fuck you Adam"
    elif ctx.author.id == 331985003644977153:
        response = "Nice"
    else:
        response = "pong"
    await ctx.message.delete()
    await ctx.channel.send(response)

#Bot connects to voice chat and
@client.command()
async def fard(ctx, arg1, arg2):
    user = ctx.message.author
    await ctx.message.delete()
    vchannel = user.voice.channel
    channel = None

    min_time = time_convert(arg1)
    max_time = time_convert(arg2)
    if min_time > max_time:
        temp_time = max_time
        max_time = min_time
        min_time = temp_time

    print(min_time, max_time)

    if (vchannel != None) and (min_time or max_time):
        channel = vchannel.name

        vc = await vchannel.connect()
        while vc.is_connected():
            random_time = random.randint(min_time, max_time)
            print(random_time)
            await asyncio.sleep(random_time)
            source = discord.FFmpegPCMAudio('fart-with-reverb.mp3')#replace with mp3 of your choice
            vc.play(source)
    else:
        await client.say('User is not in a channel.')

#NOTE: WILL CAUSE INFINITE LOOP CURRENTLY
#Sets random time between intervals or every 10 minutes. Will connect, play sound
#then disconnect.
@client.command()
async def annoy(ctx, arg1, arg2):
    annoy_boolean = True
    user = ctx.message.author
    await ctx.message.delete()
    vchannel = user.voice.channel
    channel = None

    min_time = time_convert(arg1)
    max_time = time_convert(arg2)
    if min_time > max_time:
        temp_time = max_time
        max_time = min_time
        min_time = temp_time
    print(min_time, max_time)

    if (vchannel != None) and (min_time or max_time):
        channel = vchannel.name

        while annoy_boolean:
            random_time = random.randint(min_time, max_time)
            print(random_time)
            await asyncio.sleep(random_time)
            vc = await vchannel.connect()
            source = discord.FFmpegPCMAudio('fart-with-reverb.mp3')
            vc.play(source)
            while vc.is_playing():
                await asyncio.sleep(5)
            vc.stop()
            await vc.disconnect()
    else:
        await client.say('User is not in a channel.')

#Disconnects bot if in voice chat
@client.command(pass_context = True)
async def bai(ctx):
    #Attempt to stop annoy infinite loop. Not working to how async works
    annoy_boolean = False
    for x in client.voice_clients:
        if(x.guild == ctx.message.guild):
            await ctx.message.delete()
            return await x.disconnect()

    return await ctx.channel.send("I am not connected to any voice channel on this server!")


client.run(TOKEN)
