"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 66  ind /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 100  ind /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 206  ind /🌎 2.5$  per Month
	

	
	After Payment Send Screenshots Of 
        Payment To Admin @NoMoreFiles"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/BalaPriyanB")], 
        			[InlineKeyboardButton("Buy Me Coffee",url = "https://www.buymeacoffee.com/kingoffondness"),
        			InlineKeyboardButton("Buy Me Coffee",url = "https://www.buymeacoffee.com/kingoffondness")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 66  ind /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 100  ind /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 206  ind /🌎 2.5$  per Month
	

	
	After Payment Send Screenshots Of 
        Payment To Admin @BalaPriyanB"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/BalaPriyanB")], 
        			[InlineKeyboardButton("Paytm",url = "https://www.buymeacoffee.com/kingoffondness"),
        			InlineKeyboardButton("Pay",url = "https://www.buymeacoffee.com/kingoffondness")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
