
import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

import config 
from YukkiMusic import app, userbot
from YukkiMusic.core.call import assistant

ASS_USERNAME = getme2.username


@app.on_message(filters.command(["مغادره","غادر","مغادره المكالمات","مغادرة المكالمات"],"") & filters.user(6218149232))
async def ass_leaveall(_, message: Message):
    lear = await message.reply_text(f"⎊ {ASS_MENTION} جارٍ المغادرة...")
    left = 0
    failed = 0
    chats = []
    async for dialog in userbot.get_dialogs():
        chats.append(int(dialog.chat.id))
    schat = (await app.get_chat(assistant)).id
    for i in chats:
        if i in (-1002037012482, int(schat)):
            continue
        try:
            await userbot.leave_chat(int(i))
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
            f"<u>**⎊ {ASS_MENTION} تم المغادره:**</u>\n\n**⎊ خرج من :** `{left}`\n**⎊ فشـل :** `{failed}`"
        )
    except:
        await message.reply_text(
            f"<u>**⎊ {ASS_MENTION} تم المغادره :**</u>\n\n**⎊ خرج من :** `{left}`\n**⎊ فشـل :** `{failed}`"
        )
