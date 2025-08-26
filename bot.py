print("=== BOT.PY IS LOADED ===")
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот.")

# Создание и запуск бота
from config import BOT_TOKEN
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
