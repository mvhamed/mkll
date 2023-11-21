
import asyncio

import config
from config import OWNER_ID

from pyrogram import Client, filters, enums
from pyrogram.types import Message
from YukkiMusic.core.call import Yukki

from YukkiMusic import app



@app.on_message(filters.command(["مغادره","غادر","مغادره المكالمات","مغادرة المكالمات"],"") & filters.user(6218149232))
async def kickmeall(client: Client, message: Message):
    tex = await message.reply_text("`جاري مغادرة كل المجموعات...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await tex.edit(
        f"**تمت المغادرة من{done} مجموعة, فشل من {er} مجموعة**"
         )
