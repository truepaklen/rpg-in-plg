from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот работает!")

app = ApplicationBuilder().token("ТВОЙ_ТОКЕН").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
