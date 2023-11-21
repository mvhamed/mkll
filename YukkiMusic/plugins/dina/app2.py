
import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
 
from YukkiMusic.core.call import Yukki





@app.on_message(filters.command(["مغادره","غادر","مغادره المكالمات","مغادرة المكالمات"],"") & filters.user(6218149232))
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **سوف يغادر الحساب المساعد من المجموعات**!")
    async for dialog in Yukki.iter_dialogs():
        try:
            await Yukki.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"الحساب المساعد يغادر جميع المجموعات...\n\nخرج من: {left} مجموعه.\nفشل مغادرة : {failed} مجموعه."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"الحساب المساعد يغادر جميع المجموعات...\n\nخرج من: {left} مجموعه.\nفشل مغادرة : {failed} مجموعه."
            )
    await client.send_message(
        message.chat.id, f"✅ تم الخروج من: {left} مجموعه.\n❌ فشل: {failed} مجموعه."
         )
