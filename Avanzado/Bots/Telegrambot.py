import telegram
import logging
import time
import os

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from updater import Updater

bot = telegram.Bot(token='548597358:AAHbprpAwhZQdwHJihWHRSvMdOYUVKpOFZI')
up = Updater(token='548597358:AAHbprpAwhZQdwHJihWHRSvMdOYUVKpOFZI')
dispatcher = up.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
	bot.send_message(chat_id=374038881, text='Hola creador!')

def echo(bot, update):
		bot.send_message(chat_id=374038881, text='Hola creador!')

def sendFile(bot, update, args):
	path = 'D:\\Users\\cur03alu13\\' + args[0]
	try:
		if not os.path.isfile(path):
			bot.send_message(chat_id=374038881, text='Eso no es un archivo!')
			bot.send_message(chat_id=374038881, text='Ruta = %s' % path)
		else:
			f = open(path, 'rb')
			bot.send_document(chat_id=374038881, document=f)
	except:
			bot.send_document(chat_id=374038881, text='No encontré el archivo :(')
			bot.send_message(chat_id=374038881, text='Ruta = %s' % path)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
sendFile_handler = CommandHandler('sendFile', sendFile, pass_args=True)
dispatcher.add_handler(sendFile_handler)


up.start_polling()