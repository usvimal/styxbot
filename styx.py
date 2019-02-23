import telegram
import os

TOKEN = os.environ.get("token")
bot = telegram.Bot ( token = TOKEN )

print(bot.get_me())