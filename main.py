import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# BOT TOKEN
TOKEN = "8601024606:AAHKA5r36MdnAu-83V9qUmlxsTwBD3xe84w"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men pizza narxini aytib beruvchi botman. 'pizza' yoki 'Narxa' deb yozing.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()

    if text == "pizza":
        await update.message.reply_text("pizza narxi 25000 som")
    elif text == "narxa":
        await update.message.reply_text("25000 som")

async def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    # Botni ishga tushirib turish
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
