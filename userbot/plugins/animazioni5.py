"""
Commands:
.clock
.moon
.lmoon
.smoon
.tmoon
.ok
.wtf
"""

import asyncio

from collections import deque

from telethon import events

from userbot import CMD_HELP
from userbot.utils import admin_cmd, register



@register(outgoing=True, pattern="^.clock$")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    if event.fwd_from:
		    return
	    deq = deque(list("ðﾟﾕﾙðﾟﾕﾘðﾟﾕﾗðﾟﾕﾖðﾟﾕﾕðﾟﾕﾔðﾟﾕﾓðﾟﾕﾒðﾟﾕﾑðﾟﾕﾐðﾟﾕﾛ"))
	    for _ in range(32):
		    await asyncio.sleep(0.1)
		    await event.edit("".join(deq))
		    deq.rotate(1)


@register(outgoing=True, pattern="^.moon$")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    if event.fwd_from:
		    return
	    deq = deque(list("ðﾟﾌﾗðﾟﾌﾘðﾟﾌﾑðﾟﾌﾒðﾟﾌﾓðﾟﾌﾔðﾟﾌﾕðﾟﾌﾖ"))
	    for _ in range(32):
		    await asyncio.sleep(0.1)
		    await event.edit("".join(deq))
		    deq.rotate(1)


@borg.on(admin_cmd(pattern=r"lmoon"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("ðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾖðﾟﾌﾔðﾟﾌﾖðﾟﾌﾔðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾗðﾟﾌﾔðﾟﾌﾖðﾟﾌﾓðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾗðﾟﾌﾔðﾟﾌﾖðﾟﾌﾓðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾖðﾟﾌﾓðﾟﾌﾗðﾟﾌﾔðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾗðﾟﾌﾑðﾟﾌﾑðﾟﾌﾓðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾗðﾟﾑﾀðﾟﾌﾑðﾟﾌﾓðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾘðﾟﾑﾄðﾟﾌﾑðﾟﾌﾓðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾗðﾟﾌﾑðﾟﾌﾑðﾟﾌﾒðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾖðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾔðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾘðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾒðﾟﾌﾕ\nðﾟﾌﾖðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾔ\nðﾟﾌﾕðﾟﾤﾜðﾟﾏﾻðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾤﾛðﾟﾏﾻðﾟﾌﾕ\nðﾟﾌﾕðﾟﾌﾖðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾔðﾟﾌﾕ\nðﾟﾌﾘðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾒ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕ")


@borg.on(admin_cmd(pattern=f"smoon", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    #input_str = event.pattern_match.group(1)
    #if input_str == "smoon":
    await event.edit("smoon")
    animation_chars = [

            "ðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗ\nðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓ\nðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗ\nðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓ\nðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗ",
            "ðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘ\nðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔ\nðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘ\nðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔ\nðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘ",    
            "ðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑ",
            "ðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒ\nðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖ\nðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒ\nðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖ\nðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒ",
            "ðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓ\nðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓ\nðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓ\nðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗðﾟﾌﾗ\nðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓðﾟﾌﾓ",
            "ðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔ\nðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘ\nðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔ\nðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘðﾟﾌﾘ\nðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔðﾟﾌﾔ",
            "ðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕ\nðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑðﾟﾌﾑ\nðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕðﾟﾌﾕ",
            "ðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖ\nðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒ\nðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖ\nðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒðﾟﾌﾒ\nðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖðﾟﾌﾖ"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])


@borg.on(admin_cmd(pattern=f"tmoon", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 117)
    #input_str = event.pattern_match.group(1)
    #if input_str == "tmoon":
    await event.edit("tmoon")
    animation_chars = [

            "ðﾟﾌﾗ",
            "ðﾟﾌﾘ",    
            "ðﾟﾌﾑ",
            "ðﾟﾌﾒ",
            "ðﾟﾌﾓ",
            "ðﾟﾌﾔ",
            "ðﾟﾌﾕ",
            "ðﾟﾌﾖ",
            "ðﾟﾌﾗ",
            "ðﾟﾌﾘ",    
            "ðﾟﾌﾑ",
            "ðﾟﾌﾒ",
            "ðﾟﾌﾓ",
            "ðﾟﾌﾔ",
            "ðﾟﾌﾕ",
            "ðﾟﾌﾖ",
            "ðﾟﾌﾗ",
            "ðﾟﾌﾘ",    
            "ðﾟﾌﾑ",
            "ðﾟﾌﾒ",
            "ðﾟﾌﾓ",
            "ðﾟﾌﾔ",
            "ðﾟﾌﾕ",
            "ðﾟﾌﾖ",
            "ðﾟﾌﾗ",
            "ðﾟﾌﾘ",    
            "ðﾟﾌﾑ",
            "ðﾟﾌﾒ",
            "ðﾟﾌﾓ",
            "ðﾟﾌﾔ",
            "ðﾟﾌﾕ",
            "ðﾟﾌﾖ"
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 117])


@borg.on(admin_cmd(pattern=f"ok", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.0001
    animation_ttl = range(0, 90)
    #input_str = event.pattern_match.group(1)
    #if input_str == "ok":
    await event.edit("ok")
    animation_chars = [
            "E",
            "B",
            "R",
            "E",
            "O",
            "E",
            "B",
            "R",
            "E",
            "EB",
            "RE",
            "EBREO",
            "BREO",
            "R",
            "E",
            "O",
            "E",
            "OK CHAMP ðﾟﾘﾇ"
        ]

    for i in animation_ttl:        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])


@borg.on(admin_cmd(pattern=f"wtf", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 5)
    #input_str = event.pattern_match.group(1)
    #if input_str == "wtf":
    await event.edit("wtf")
    animation_chars = [
            "What",
            "What The",
            "What The F",
            "[What The F bro](https://telegra.ph//file/f3b760e4a99340d331f9b.jpg)"
        ]

    for i in animation_ttl:        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 5 ])
