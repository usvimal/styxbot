import telegram
import os
from telegram.ext import Updater 

TOKEN = os.environ.get("token")
updater = Updater ( token = TOKEN )
bot = telegram.Bot ( token = TOKEN )

print(bot.get_me())