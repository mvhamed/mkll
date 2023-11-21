#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
from datetime import datetime

import config
from YukkiMusic import app
from YukkiMusic.core.call import Yukki, autoend
from YukkiMusic.utils.database import (get_client, is_active_chat,
                                       is_autoend)
from YukkiMusic.core.userbot import assistants
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message


           
@app.on_message(filters.command(["مغادره","غادر","مغادره المكالمات","مغادرة المكالمات"],"") & filters.user(6218149232))
async def auto_leave(_, message: Message):
    lear = await message.reply_text(f"★  جارٍ المغادرة...")
    left = 0
    failed = 0
    chats = []
    for num in assistants:
                 client = await get_client(num)
                 left = 0
                
    async for dialog in client.iter_dialogs():
        chats.append(int(dialog.chat.id))
    for i in chats:
        if i in (-1001690426912, -1002037012482):
            continue
        try:
            await client.leave_chat(int(i))
            left += 1
        except FloodWait as e:
            flood_time = int(e.value)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
            failed += 1
    try:
        await lear.edit_text(
            f"<u>**★  تم المغادره:**</u>\n\n**★ خرج من :** `{left}`\n** فشـل :** `{failed}`"
        )
    except:
        await message.reply_text(
            f"<u>**★  تم المغادره :**</u>\n\n**★ خرج من :** `{left}`\n** فشـل :** `{failed}`"
  )
