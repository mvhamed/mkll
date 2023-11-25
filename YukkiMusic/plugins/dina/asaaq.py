import asyncio

import os
import requests
from config import OWNER_ID
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from random import  choice, randint
from typing import Union


@app.on_message(
  filters.command(["المطور"],"")
  
)
async def yas(client, message):
    usr = await client.get_chat("Asaaql7")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**معلومات المطور الاساسي\n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                 ], [
                    InlineKeyboardButton(
                        "قناة المطور", url=f"https://t.me/Mlze1bot"),                        
                 ],
            ]
        ),
    )

RAEAK = ["زينه","حلوه","فخمه","جميله","خوش","انيقه","مو حلوه","بشعه","مو زينه","كلش حلوه","استمر بيها","احبها","غيرها حباب"]


@app.on_message(filters.command(["صورتي","رائي دينا بصورتك"],"")) 
async def madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""صورتك {choice(RAEAK)} 🧸♥️""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
      )
