import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
from asyncio import gather



@app.on_message(
    filters.command(["بايو","البايو"],""))
async def biio(client, message):
  nq = await client.get_chat(message.from_user.id)
  bio = nq.bio
  await message.reply_text(bio
  )
