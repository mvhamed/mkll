import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app, Telegram
import random
from config import ASAAQ_CHANNEL, YAFA_NAME


@app.on_message(filters.command([f"زومل", "زامل", "عيسى الليث", "{BOT_USERNAME} زامل"],"") & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/zwamlallaith/{rl}"
    await client.send_voice(message.chat.id,url,caption="عزيزي   \n ✧   [{YAFA_NAME}]({ASAAQ_CHANNEL}) ",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["انمي","صور انمي"],"")) 
async def ihd(client: Client, message: Message):
    rs = random.randint(166,212)
    url = f"https://t.me/aftarat56/{rs}"
    await client.send_photo(message.chat.id,url,caption="✧---------✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](t.me/Mlze1bot) ",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

                        
@app.on_message(filters.command([f"شيله", "بدر العزي", "شيلات", "{BOT_USERNAME} شيلات"],"") & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/Alezzi1/{rl}"
    await client.send_voice(message.chat.id,url,caption="---------✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](t.me/Mlze1bot)",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂", url=f"t.me/Mlze1bot")
                ],
            ]
        )
    )

@app.on_message(filters.command(["أغاني", "غنيلي 🧚‍♂️"],"") & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/MusicIsaac/{rl}"
    await client.send_voice(message.chat.id,url,caption="✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](t.me/Mlze1bot)  ",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂", url=f"t.me/Mlze1bot")
                ],
            ]
        )
    )
@app.on_message(filters.command(["فيلم", "فيلمك"],""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,34)
    url = f"https://t.me/gyigkk/{rl}"
    await client.send_audio(message.chat.id,url,caption="✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](t.me/Mlze1bot)  ",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
@app.on_message(filters.command(["برمجيه","صور برمجيه"],"")) 
async def ihd(client: Client, message: Message):
    rs = random.randint(215,267)
    url = f"https://t.me/aftarat56/{rs}"
    await client.send_photo(message.chat.id,url,caption="✧---------✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](t.me/Mlze1bot) ",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
      )
@app.on_message(filters.command(["خلفيات للهاتف","خلفيات فخمه"],"")) 
async def ihd(client: Client, message: Message):
    rs = random.randint(270,312)
    url = f"https://t.me/aftarat56/{rs}"
    await client.send_photo(message.chat.id,url,caption="✧---------✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂](t.me/Mlze1bot) ",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
        )
