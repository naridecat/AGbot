# -*- conding: utf-8 -*-
import discord
import random
import asyncio
from discord.utils import get

client = discord.Client()
player = []
stop = 0
whoid = 0
minitype = 0
input_num = 0
afk = []
ban = []
final_num = 0
pt = 0
@client.event
async def on_ready(): print("ready")

@client.event
async def on_message(message):
    global player
    global stop
    global whoid
    global minitype
    global final_num
    global ban
    global input_num
    global afk
    global pt
    if message.author.id == 관리자id and message.content == "!br31":
        await message.delete()
        while True:
            stop = 0
            whoid = 0
            minitype = 0
            final_num = 0
            embed = discord.Embed(title="AG. BR31", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``20초 기다리는 중``", color=0x00c8c8)
            message = await message.channel.send(embed=embed)
            await message.add_reaction("이모지 <::>")
            await asyncio.sleep(5)
            embed = discord.Embed(title="AG. BR31", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``15초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(5)
            embed = discord.Embed(title="AG. BR31", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``10초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(5)
            embed = discord.Embed(title="AG. BR31", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``5초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(1)
            embed = discord.Embed(title="AG. BR31", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``4초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(1)
            embed = discord.Embed(title="AG. BR31", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``3초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(1)
            embed = discord.Embed(title="AG. BR31", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``2초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(1)
            embed = discord.Embed(title="AG. BR31", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``1초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await message.delete()
            if len(player) > 2:
                for i in range(len(player)):
                    r = await message.guild.fetch_member(int(player[i]))
                    role = get(message.guild.roles, id=게임 진행시 받을 역할 id)
                    await r.add_roles(role)
            # 미니게임 부분 시작
                while True:
                    minitype = 2
                    if minitype == 2:
                        input_num = 0
                        whoid = 0
                        stop = 0
                        pt = 0
                        afk = []
                        ban = []
                        embed = discord.Embed(title="베라31", description="**게임방법**\n\n1부터 31까지의 수를 순서대로 입력합니다.\n한번에 총 3번 연속으로 수를 입력할 수 있습니다.\n31을 가장 처음 말하는 사람이 게임에서 이깁니다.\n``!(1~3)``로 수를 입력할 수 있습니다.\n2번 제한시간동안 입력하지 않으면 게임에서 자동으로 제외됩니다.")
                        await message.channel.send(embed = embed)
                        while True:
                            if len(ban) == len(player):
                                break
                            for i in range(len(player)):
                                if player[i] in ban:
                                    continue
                                await message.channel.send("<@"+str(player[i])+"> 차례입니다.")
                                whoid = player[i]
                                await asyncio.sleep(10)
                                if input_num != 0:
                                    for j in range(int(input_num)):
                                        pt = pt+1
                                        if pt == 31:
                                            stop = 1
                                            break
                                        input_num = 0
                                        await message.channel.send(pt)
                                else:
                                    if player[i] in afk:
                                        ban.append(player[i])
                                    else:
                                        afk.append(player[i])
                                if stop == 1:
                                    break
                            if stop == 1:
                                await message.channel.send("우승자 : <@"+str(player[i])+">")
                                break
                        await asyncio.sleep(1)
                        for i in range(len(player)):
                            r = await message.guild.fetch_member(int(player[i]))
                            role = get(message.guild.roles, id=  게임 진행시 빋은 역할 id)
                            await r.remove_roles(role)
                        async for msg in message.channel.history():
                            await msg.delete()
                        break
                    if minitype == 3:
                        input_num = 0
                        whoid = 0
                        stop = 0
                        pt = 0
                        afk = []
                        ban = []
                        embed = discord.Embed(title="초성게임", description="**게임방법**\n\n봇이 제시하는 초성의 글자를 \n2번 제한시간동안 입력하지 않으면 게임에서 자동으로 제외됩니다.")
                        await message.channel.send(embed = embed)
                    # 미니게임 부분 종료
            player = []
            await asyncio.sleep(1)
    if minitype == 2 and message.author.id == int(whoid) and input_num == 0 and message.content.startswith("!") and stop == 0:
        d = message.content[1:]
        if d.isdigit:
            if int(d) > 0 and int(d) < 4:
                input_num = d
                await message.channel.send("<@"+str(message.author.id)+"> "+d+" 입력됨")
@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji.id == 참여시 누를 이모지 id and user.id !== 봇 자기자신 id:
        player.append(user.id)

@client.event
async def on_reaction_remove(reaction, user):
    if reaction.emoji.id == 참여시 누를 이모지 id:
        player.remove(user.id)
client.run("token")
