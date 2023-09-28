import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6055223043:AAE4yj8Tptg2vCCQfsw5HAB3cA0tc_ZTsr4")

API_ID = int(os.environ.get("API_ID", "9830058"))

API_HASH = os.environ.get("API_HASH", "908e8bff7c8f6ecd5d0ab989f78134fc")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
