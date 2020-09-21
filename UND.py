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
    if message.author.id == 관리자id and message.content == "!und":
        await message.delete()
        while True:
            stop = 0
            whoid = 0
            minitype = 0
            final_num = 0
            embed = discord.Embed(title="AG. U&D", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``20초 기다리는 중``", color=0x00c8c8)
            message = await message.channel.send(embed=embed)
            await message.add_reaction("이모지<::>")
            await asyncio.sleep(5)
            embed = discord.Embed(title="AG. U&D", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``15초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(5)
            embed = discord.Embed(title="AG. U&D", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``10초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(5)
            embed = discord.Embed(title="AG. U&D", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``5초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(1)
            embed = discord.Embed(title="AG. U&D", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``4초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(1)
            embed = discord.Embed(title="AG. U&D", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``3초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(1)
            embed = discord.Embed(title="AG. U&D", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``2초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await asyncio.sleep(1)
            embed = discord.Embed(title="AG. U&D", description="**플레이어를 기다리고 있습니다.**\n\n> 참여하려면 __**반응**__을 눌러주세요\n3명이상 모이면 시작하겠습니다!\n\n``1초 기다리는 중``", color=0x00c8c8)
            await message.edit(embed = embed)
            await message.delete()
            if len(player) > 2:
                for i in range(len(player)):
                    r = await message.guild.fetch_member(int(player[i]))
                    role = get(message.guild.roles, id=게임시 줄 역할id)
                    await r.add_roles(role)
            # 미니게임 부분 시작
                while True:
                    minitype = 1
                    if minitype == 1: # 업앤다운 시작
                        input_num = 0
                        final_num = 0
                        whoid = 0
                        stop = 0
                        afk = []
                        ban = []
                        embed = discord.Embed(title="업앤다운", description="**게임방법**\n\n1~50까지 숫자중 랜덤한 숫자 하나가 선택되며, 플레이어는 돌아가며 숫자를 입력하며,\n플레이어가 제시한 숫자가 정해진 숫자보다 높으면 다운, 낮으면 업이라고 출력됩니다.\n랜덤한 숫자를 가장 먼저 맞추면 점수를 얻습니다.\n자신의 차례에 ``!(숫자)``를 입력하여 숫자를 입력할 수 있습니다.\n2번 제한시간동안 입력하지 않으면 게임에서 자동으로 제외됩니다.")
                        await message.channel.send(embed = embed)
                        final_num = random.randint(1,50)
                        while True:
                            if len(player) == len(ban):
                                break
                            for i in range(len(player)):
                                if player[i] in ban:
                                    continue
                                await message.channel.send("<@"+str(player[i])+"> 차례입니다.")
                                whoid = player[i]
                                await asyncio.sleep(10)
                                if stop == 0:
                                    if input_num == 0: # player[i]가 10초동안 잠수를 탈때
                                        if player[i] in afk:
                                            ban.append(player[i])
                                        else:
                                            afk.append(player[i])
                                        continue
                                    elif input_num > final_num:
                                        await message.channel.send(message.content + " 다운!")
                                        input_num = 0
                                    elif input_num < final_num:
                                        await message.channel.send(message.content + " 업!!")
                                        input_num = 0
                                    continue
                                else:
                                    await message.channel.send("우승자 : <@"+str(player[i])+">")
                                    await asyncio.sleep(3)
                                    break
                            if stop==1:
                                break
                        for i in range(len(player)):
                            r = await message.guild.fetch_member(int(player[i]))
                            role = get(message.guild.roles, id=게임시 준 역할id)
                            await r.remove_roles(role)
                        async for msg in message.channel.history():
                            await msg.delete()
                        break
                    # 미니게임 부분 종료
            player = []
            await asyncio.sleep(1)
    if minitype == 1 and message.author.id == int(whoid) and input_num == 0 and message.content.startswith("!") and stop == 0:
        d = message.content[1:]
        if d.isdigit:
            if int(d) == final_num:
                stop = 1
            input_num = int(d)
            await message.channel.send("<@"+str(message.author.id)+"> "+d+" 입력됨")
@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji.id == 이모지id and user.id != 봇id:
        player.append(user.id)

@client.event
async def on_reaction_remove(reaction, user):
    if not isinstance(user, str):
        if reaction.emoji.id == 이모지id:
            player.remove(user.id)
client.run(Token)
