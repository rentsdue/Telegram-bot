from typing import Final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ContextTypes, Application

# Token: Define a constant variable 'TOKEN' with the Telegram Bot API token as its value.
TOKEN: Final = '6430569246:AAHOqlsBSKvrAV0wbun5pzXdNlmZUgOO1KY'

# Username: Define a constant variable 'BOT_USERNAME' with the bot's username as its value.
BOT_USERNAME: Final = '@Thebotsonbot'

# Commands: Define an asynchronous function 'start' that takes two arguments: 'update' of type 'Update',
# representing an incoming update from Telegram, and 'context' of type 'ContextTypes.DEFAULT_TYPE'.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /start command."""
    await update.message.reply_text("Hello there. How can I help you?")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /help command."""
    await update.message.reply_text("I am a bot. How can I help you?")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /about command."""
    await update.message.reply_text("This is a telegram bot designed to respond to basic commands. I can respond uniquely to a wide range of prompts!")

async def sentencereverse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /sentencereverse command."""
    await update.message.reply_text("Please send me a message, and I'll reverse the words in it.")
    if update.message and update.message.text:
        user_message = update.message.text
        words = user_message.split()
        reversed_message = ' '.join(reversed(words))
        await update.message.reply_text(f"Reversed message: {reversed_message}")
    else:
        await update.message.reply_text("Try again!")

async def wordreverse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /wordreverse command."""
    await update.message.reply_text("Please send a single word and I'll reverse it!")
    if update.message and update.message.text:
        user_message = update.message.text
        words = user_message.split()
        if len(words) > 1:
            await update.message.reply_text("Please input a single word only!")
        else:
            reversed_word = words[0][::-1]
            await update.message.reply_text(f"Reversed word: {reversed_word}")

# Define app:
app = Application.builder().token(TOKEN).build()

# Add command handlers
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(CommandHandler('about', about))
app.add_handler(CommandHandler('sentencereverse', sentencereverse))
app.add_handler(CommandHandler('wordreverse', wordreverse))

# Responses
def responsehandling(text: str) -> str:
    """Handle user messages and provide responses."""
    user_message = text.lower()
    responses = {
        "hello": "Hello there.",
        "how are you": "I'm doing fine, thank you very much for asking.",
        "thank": "You're welcome! I'm just doing my job!",
        "excuse me": "What can I do for you?",
        "sorry": "It's alright!"
    }
    
    # Check for exact matches first
    for keyword, response in responses.items():
        if keyword == user_message:
            return response

    # Check for partial matches
    for keyword, response in responses.items():
        if keyword in user_message:
            return response

    # If no matches found, respond with a default message
    return "I'm here to assist you. Please feel free to ask any questions or use commands."

# Respond handlers
app.add_handler(MessageHandler(filters.TEXT, responsehandling))