import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import bot, CMD_HELP

from userbot import bot, CMD_HELP
import io
import math
import urllib.request
from os import remove
from userbot.events import register
import io
import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument

from PIL import Image
import random
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from userbot import bot, CMD_HELP
import io
import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
from telethon.tl.types import DocumentAttributeSticker
from userbot import CMD_HELP, ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "I'M STUPID"


@register(outgoing=True, pattern="^.ext3(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a foto/sticker**")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a foto/sticker**")
       return
    chat = "@hazmat_suit_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit(f"`{DEFAULTUSER}:`**Rispondi a un user, no al bot.**")
       return
    await event.edit(f"`{DEFAULTUSER}:`**Creo Stickers...**")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=905164246))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please sblocca @hazmat_suit_bot ```")
              return
          if response.text.startswith("Forward"):
             await event.edit(f"`{DEFAULTUSER}:`**privacy error**")
          else:
          	if response.text.startswith("Select"):
          		await event.edit(f"`{DEFAULTUSER}:`Please vai su @DrWebBot e select la lingua.") 
          	else: 
          			await bot.send_file(event.chat_id, response.message.media)

