import os
import random
from discord.voice_client import VoiceClient
import discord
from discord.ext import commands
from config import settings
import asyncio
import datetime as dt
from discord.ext.commands import Bot
import time
from func import picture

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())
# client = discord.Client(intents=discord.Intents.default())
blackList = [697346435254845470]
whiteList = [690615152722313317,
             506401274653179916,
             549954069012152354]
niggerList = [505020620078317570]
alli = [690615152722313317, 506401274653179916, 549954069012152354, 505020620078317570, 697346435254845470,
        431773128478425088, 697516828464906353]
commanda= ["!cheap", "!govno", "!stupid", "!right", "!dinner_time", "!leavee" ]

506401274653179916
@client.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None:
        if after.channel.id == 914801860454527006:
            return
    if not before.channel and after.channel and (member.id == 697516828464906353):
        connected = member.voice
        pic = picture()

        await client.get_channel(907541957402853430).send(file=discord.File('picture/'+pic), delete_after=300.0)
        # if connected:
        #     vc = await connected.channel.connect()
        #     vc.play(discord.FFmpegPCMAudio(source="papich.mp4"))
        # while vc.is_playing():
        #     time.sleep(1)
        # await vc.disconnect()
    if not before.channel and after.channel and (member.id in blackList):
        connected = member.voice
        # if connected:
        #     vc = await connected.channel.connect()
        #     time.sleep(1)
        #     vc.play(discord.FFmpegPCMAudio(source="nohappy.mp4"))
        # while vc.is_playing():
        #     time.sleep(1)
        # await vc.disconnect()
        await member.move_to(client.get_channel(914801860454527006))
    if not before.channel and after.channel and (member.id == 697516828464906353):
        await client.get_channel(907541957402853430).send(file=discord.File('4.jpg'), delete_after=900.0)


@client.event
async def on_message(messag):
    ofn = 0
    commandq = messag.content
    command = commandq.split(" ", 1)
    if command[0] == "!cheap":
        await messag.delete()
        connected = messag.author.voice
        if connected:
            if len(command) == 2:
                try:
                    id = int(command[1])
                    print(id)
                    if id in alli:
                        await messag.channel.send("<@{}>".format(command[1]) + 'пойман за руку, как дешёвка.')
                except:
                    print("ошибка")
            vc = await connected.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="cheap.mp4"))
            while vc.is_playing():
                time.sleep(1)
            await vc.disconnect()
        else:
            await messag.channel.send(
                "Пошли выйдем раз на раз в голосовой! Или зассал? Как на месте будешь позови снова")

    if command[0] == "!govno":
        await messag.delete()
        connected = messag.author.voice
        if connected:
            if len(command) == 2:
                try:
                    id = int(command[1])
                    print(id)
                    if id in alli:
                        await messag.channel.send("<@{}>".format(command[1]) + ' тупое гавно.')
                except:
                    print("ошибка")
            vc = await connected.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="govno.mp4"))
            while vc.is_playing():
                time.sleep(1)
            await vc.disconnect()
        else:
            await messag.channel.send(
                "Пошли выйдем раз на раз в голосовой! Или зассал? Как на месте будешь позови снова")

    if command[0] == "!stupid":
        await messag.delete()
        connected = messag.author.voice
        if connected:
            if len(command) == 2:
                try:
                    id = int(command[1])
                    print(id)
                    if id in alli:
                        await messag.channel.send("<@{}>".format(command[1]) + ' Слушай, это тебе объясняют.')
                except:
                    print("ошибка")
            vc = await connected.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="stupid.mp4"))
            while vc.is_playing():
                time.sleep(1)
            await vc.disconnect()
        else:
            await messag.channel.send(
                "Пошли выйдем раз на раз в голосовой! Или зассал? Как на месте будешь позови снова")
    if command[0] == "!right":
        await messag.delete()
        connected = messag.author.voice
        if connected:
            if len(command) == 2:
                ofn = 1
            vc = await connected.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="right.mp4"))
            while vc.is_playing():
                time.sleep(1)
            if ofn == 1:
                await messag.channel.send(command[1], tts=True)
                ofn = 0
            await vc.disconnect()
        else:
            await messag.channel.send(
                "Пошли выйдем раз на раз в голосовой! Или зассал? Как на месте будешь позови снова")
    if command[0] == "!leavee":
        await messag.delete()
        connected = messag.author.voice
        if connected:
            if len(command) == 2:
                try:
                    id = int(command[1])
                    print(id)
                    if id in alli:
                        await messag.channel.send("<@{}>".format(command[1]) + 'выйди отсюда.')
                except:
                    print("ошибка")
            vc = await connected.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="1231.mp4"))
            while vc.is_playing():
                time.sleep(1)
            await vc.disconnect()
        else:
            await messag.channel.send(
                "Пошли выйдем раз на раз в голосовой! Или зассал? Как на месте будешь позови снова")

    if messag.content == "!dinner_time":
        await messag.delete()
        await messag.channel.send(file=discord.File('file/dinner.png'), delete_after=900.0)

    if messag.author.id in blackList and messag.content not in commanda:
        await messag.add_reaction('😇')
        await messag.channel.send(file=discord.File('file/image1.png'), delete_after=900.0)
        await messag.channel.send("Блять, опять упал писюн квадратный!")

    if messag.author.id in whiteList and messag.content not in commanda:
        await  messag.channel.send("Он хорош, очень хорош!", delete_after=900.0)

    if messag.author.id in niggerList and messag.content not in commanda:
        await  messag.channel.send("А ты не хорош", delete_after=900.0)


@client.event
async def on_raw_reaction_add(payload):
    channelid = payload.channel_id
    user = payload.member
    userid = payload.member.id
    messageid = payload.message_id
    ran = random.random()
    print(ran)
    if userid in blackList:
        if ran >0.05:
            channel = client.get_channel(channelid)
            message = await channel.fetch_message(messageid)
            for reaction in message.reactions:
                await reaction.remove(user)
    else:
        return


client.run('MTExOTM0ODg2MTY4OTkyOTc0OQ.GQYzCP.VnoBs8QpyHMzsOMaEPbNzhl7eUtuDuiH-edo9c')


