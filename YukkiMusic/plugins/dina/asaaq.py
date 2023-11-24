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

@app.on_message(
  filters.command(["المطور"],"")
  
)
async def yas(client, message):
    usr = await client.get_chat(OWNER_ID)
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
