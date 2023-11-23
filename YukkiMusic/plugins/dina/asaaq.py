from pyrogram import * 
from pyrogram.types import * 
from YukkiMusic import app
import time
from config import BOT_TOKEN, OWNER_ID
import requests
import json 

token = (BOT_TOKEN)

bot_id = app.bot_token.split(":")[0]
dev_owner = (OWNER_ID)
owner = (OWNER_ID) 


@app.on_message(filters.command(["اذاعه للكل"],""))
async def AllCommand__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner or int(user) == dev_owner:
		await m.delete()
		ask = await m.reply(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		else:
			users = open(f"Users{bot_id}.json","r")
			groups = open(f"groups{bot_id}.json","r")
			bans = open(f"band{bot_id}.json","r")
			
			for user in users:
				try:
					await ask.copy(int(user),
					inputText,
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
				
			for group in groups:
				try:
					await ask.copy(int(group),
					inputText,
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			
			for ban in bans:
				try:
					await ask.copy(int(ban),
					inputText,
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
				
			x1 = len(open(f"Users{bot_id}.json","r").readlines())
			x2 = len(open(f"band{bot_id}.json","r").readlines())
			x3 = len(open(f"groups{bot_id}.json","r").readlines())
			
			
			await app.send_message(chat,
			f"**تم الاذاعه الي** : \n\n {x1} من الأعضاء \n {x2} من المحظورين \n {x3} من المجموعات")

