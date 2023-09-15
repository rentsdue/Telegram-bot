from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()

# Get the TOKEN from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

#Command that says hello to the user
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

#Command that greets the user
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a bot. How can I help you?")

#Command that describes the bot itself
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a telegram bot designed to respond to basic commands. I can respond uniquely to a wide range of prompts!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler('help', help))
app.add_handler(CommandHandler('about', about))
app.add_handler(CommandHandler('sentencereverse', sentencereverse))
app.add_handler(CommandHandler('wordreverse', wordreverse))

app.run_polling()
