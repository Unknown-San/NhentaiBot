from API.starter import start
from API.nhentai import Nhentai
from config import bot

try:
    Nhentai()
    
except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
