﻿"""Emoji
Available Commands:
.fadmin"""

from telethon import events
from userbot.utils import admin_cmd
import asyncio



@borg.on(admin_cmd(pattern=f"fadmin", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "fadmin":

        await event.edit(input_str)

        animation_chars = [
        
            "**Promozione User ad Admin...**",
            "**Attivazione di tutti i Permessi...**",
            "**(1) Inviare Messaggi: ☑️**",
            "**(1) Inviare Messaggi: ✅**",
            "**(2) Inviare Media: ☑️**",
            "**(2) Inviare Media: ✅**",
            "**(3) Inviare stickers & GIF: ☑️**",
            "**(3) Inviare stickers & GIF: ✅**",    
            "**(4) Inviare sondaggi: ☑️**",
            "**(4) Inviare sondaggi: ✅**",
            "**(5) Inviare link con anteprima: ☑️**",
            "**(5) Inviare link con anteprima: ✅**",
            "**(6) Aggiungere utenti: ☑️**",
            "**(6) Aggiungere utenti: ✅**",
            "**(7) Fissare messaggi: ☑️**",
            "**(7) Fissare messaggi: ✅**",
            "**(8) Cambiare le info chat: ☑️**",
            "**(8) Cambiare le info chat: ✅**",
            "**Permessi attivati con successo**",
            "**Promosso con Successo da: @sethgld**"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])
