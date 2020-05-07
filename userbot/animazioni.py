"""
Available Commands:
.bombs
.fuck
.kiss
.love
.pornhub
.sex
.sexy
"""

from telethon import events

from userbot.utils import admin_cmd

import asyncio



@borg.on(admin_cmd(pattern=f"bombs", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("ðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \nðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \nðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \nðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \nðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣðﾟﾒﾣ \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \nðﾟﾒﾥðﾟﾒﾥðﾟﾒﾥðﾟﾒﾥ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \nðﾟﾒﾥðﾟﾒﾥðﾟﾒﾥðﾟﾒﾥ \nðﾟﾒﾥðﾟﾒﾥðﾟﾒﾥðﾟﾒﾥ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \nðﾟﾘﾵðﾟﾘﾵðﾟﾘﾵðﾟﾘﾵ \n")
    await asyncio.sleep(0.5)
    await event.edit("`RIP ðﾟﾘﾵðﾟﾘﾵðﾟﾘﾵ...`")
    await asyncio.sleep(2)
    

@borg.on(admin_cmd(pattern=f"fuck", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "fuck":
    await event.edit("fuck")
    animation_chars = [

            "ðﾟﾑﾉ       ✊️",

            "ðﾟﾑﾉ     ✊️",

            "ðﾟﾑﾉ  ✊️",

            "ðﾟﾑﾉ✊️ðﾟﾒﾦ"

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd(pattern="love", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.0
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "love":
    await event.edit("love")
    animation_chars = [

            "L_",

            "LO_",

            "LOV_",
            
            "LOVE_",
            
            "LOVE❤",
            

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])



@borg.on(admin_cmd(pattern=f"kiss", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "kiss":
    await event.edit("kiss")
    animation_chars = [

            "ðﾟﾤﾵ       ðﾟﾑﾰ",

            "ðﾟﾤﾵ     ðﾟﾑﾰ",

            "ðﾟﾤﾵ  ðﾟﾑﾰ",

            "ðﾟﾤﾵðﾟﾒﾋðﾟﾑﾰ"

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd(pattern="pornhub", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.0
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "pornhub":
    await event.edit("pornhub")
    animation_chars = [

            "P_",

            "PO_",

            "POR_",

            "PORN_",
            
            "PORNH_",
            
            "PORNHU_",
            
           "PORNHUB_", 
           
           "PORNHUB",

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])


@borg.on(admin_cmd(pattern=f"sex", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "sex":
    await event.edit("sex")
    animation_chars = [

            "ðﾟﾤﾵ       ðﾟﾑﾰ",

            "ðﾟﾤﾵ     ðﾟﾑﾰ",

            "ðﾟﾤﾵ  ðﾟﾑﾰ",

            "ðﾟﾤﾵðﾟﾑﾼðﾟﾑﾰ"

        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd(pattern="sexy", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.0
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "sexy":
    await event.edit("sexy")
    animation_chars = [

            "S_",

            "SE_",

            "SEX_",

            "SEXY_",
            
            "SEXYðﾟﾑﾄ_",
            
            "SEXYðﾟﾑﾄ",
            
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 10])
