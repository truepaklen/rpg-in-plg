import sys
print("✅ Python version:", sys.version)
from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN

def start(update, context):
    update.message.reply_text("Привет! Я бот.")

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
