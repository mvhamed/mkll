import random
import os
import random
import requests
import asyncio
import re
from cgi import print_arguments
from pyrogram import Client, filters
from config import BANNED_USERS
from strings import get_command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from YukkiMusic import settingsApp
from strings import get_command

    
disable = []

flex = {}
chat_watcher_group = 3
         
         
@app.on_message(filters.command("تعطيل غنيلي", [".", ""]) & filters.group)
async def deslink(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id in disable:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable.append(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تعطيل امر غنيلي**") 
         
         
@app.on_message(filters.command("تفعيل غنيلي", [".", ""]) & filters.group)
async def enablelink(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id not in disable:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable.remove(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تفعيل امر غنيلي**")         
         
@app.on_message(filters.regex("^غنيلي$") & filters.group)
async def musicme(client, message):
       if message.chat.id in disable:
         return await message.reply_text("**- تم تعطيل امر غنيلي من قبل المشرفين**")
       if message.chat.id not in disable:
         rl = random.randint(3,200)
         url = f"https://t.me/MusicIsaac/{rl}"
         await message.reply_voice(url,caption="-› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂  •](t.me/Mlze1bot)")
         


disable_A = []

flex = {}
chat_watcher_group = 3
         
         
@app.on_message(filters.command("تعطيل الافتارات", [".", ""]) & filters.group)
async def avtarB(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id in disable_A:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_A.append(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تعطيل اوامر الافتارات**") 
         
         
@app.on_message(filters.command("تفعيل الافتارات", [".", ""]) & filters.group)
async def AvtarT(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id not in disable_A:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_A.remove(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تفعيل اوامر الافتارات**")         
         
@app.on_message(filters.regex("^افتار عيال$") & filters.group)
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتار عيال من قبل المشرفين\n- للتفعيل اكتب تفعيل الافتارات**")
       if message.chat.id not in disable_A:
         rl = random.randint(63,126)
         url = f"https://t.me/mcsec8/{rl}"
         await message.reply_photo(url,caption="-› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂  •](t.me/Mlze1bot)")
         
@app.on_message(filters.regex("^افتارات عيال$"))
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتارات عيال من قبل المشرفين\n- للتفعيل اكتب تفعيل الافتارات**")
       if message.chat.id not in disable_A:
         rl = random.randint(63,128)
         url = f"https://t.me/mcsec8/{rl}"
         await message.reply_photo(url,caption="-› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂  •](t.me/Mlze1bot)")
         
         
@app.on_message(filters.regex("^افتار بنات$"))
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتار بنات من قبل المشرفين\n- للتفعيل اكتب تفعيل الافتارات**")
       if message.chat.id not in disable_A:
         rl = random.randint(3,62)
         url = f"https://t.me/mcsec8/{rl}"
         await message.reply_photo(url,caption="-› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂  •](t.me/Mlze1bot)")
         
@app.on_message(filters.regex("^افتارات بنات$"))
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتارات بنات من قبل المشرفين\n- للتفعيل اكتب تفعيل الافتارات**")
       if message.chat.id not in disable_A:
         rl = random.randint(3,62)
         url = f"https://t.me/mcsec8/{rl}"
         await message.reply_photo(url,caption="-› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂  •](t.me/Mlze1bot)")
         
@app.on_message(filters.regex("^افتارات مكس$"))
async def ava(client, message):
       if message.chat.id in disable_A:
         return await message.reply_text("**- تم تعطيل امر افتارات مكس من قبل المشرفين**")
       if message.chat.id not in disable_A:
         rl = random.randint(3,129)
         url = f"https://t.me/mcsec8/{rl}"
         await message.reply_photo(url,caption="-› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂 •](t.me/Mlze1bot)")
         



disable_h = []

flex = {}
chat_watcher_group = 3
         
         
@app.on_message(filters.command("تعطيل الهيدرات", [".", ""]) & filters.group)
async def hy1(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id in disable_h:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_h.append(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تعطيل امر هيدرات**") 
         
         
@app.on_message(filters.command("تفعيل الهيدرات", [".", ""]) & filters.group)
async def hy(client, message):      
       a = await app.get_chat_member(message.chat.id, message.from_user.id)
       if message.chat.id not in disable_h:
         return

       if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
        
       if a.can_manage_chat:
         disable_h.remove(message.chat.id)
         await message.reply_text(f"- ابشر عيني {message.from_user.mention}\n**- تم تفعيل امر هيدرات ~ هيدر**") 



@app.on_message(filters.regex("^هيدرات$") & filters.group)
async def hyder(client, message):
       if message.chat.id in disable_h:
         return await message.reply_text("**- تم تعطيل امر هيدرات من قبل المشرفين\n- للتفعيل اكتب تفعيل الهيدرات**")
       if message.chat.id not in disable_h:
         rl = random.randint(3,1111)
         url = f"https://t.me/HayderTwitter/{rl}"
         await message.reply_photo(url,caption="-› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂  •](t.me/Mlze1bot)")


@app.on_message(filters.regex("^هيدرات$"))
async def hyder1(client, message):
       if message.chat.id in disable_h:
         return await message.reply_text("**- تم تعطيل امر هيدرات من قبل المشرفين\n- للتفعيل اكتب تفعيل الهيدرات**")
       if message.chat.id not in disable_h:
         rl = random.randint(5,1170)
         url = f"https://t.me/HayderTwitter/{rl}"
         await message.reply_photo(url,caption="-› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂  •](t.me/Mlze1bot)")
