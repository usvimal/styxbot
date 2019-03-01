import telegram
import os
import logging
import time
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

log = logging.getLogger(__name__)

TOKEN = os.environ.get("token")
bot = telegram.Bot(token=TOKEN)

print(bot.get_me())


def start(bot, update):
	update.message.reply_text("Hello there, General Kenobi")


def error(bot, update, error):
	"""Log Errors caused by Updates."""
	log.warning('Update "%s" caused error "%s"', update, error)


def ping(bot, update):
	pingtime = time.time()
	ping: float = time.time() - pingtime
	await update.message.reply_text(" time is `%.03f seconds` :ping_pong:" % ping)


def main():
	updater = Updater(token=TOKEN)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', start))

	# log all errors
	dispatcher.add_error_handler(error)

	# start the bot
	updater.start_polling()

	updater.idle()


if __name__ == '__main__':
	main()
