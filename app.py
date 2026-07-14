print("Study Notes Bot Started")
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8287953535:AAHprlO_nvwkER-NmXU0Xsma1ReBUurHjtQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot chal raha hai.")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
