from typing import Final  # Import the Final type hint from the 'typing' module.

from telegram import Update  # Import the 'Update' class from the 'telegram' module.
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes #Imports various classes from the "telegram" module.

TOKEN: Final = '6430569246:AAHOqlsBSKvrAV0wbun5pzXdNlmZUgOO1KY' #Define a constant variable 'TOKEN' with the Telegram Bot API token as its value. 'Final' is used to indicate that this variable should not be reassigned.

# Define a constant variable 'BOT_USERNAME' with the bot's username as its value.
BOT_USERNAME: Final = '@Thebotsonbot'

# Define an asynchronous function 'startcommand' that takes two arguments:
# 'update' of type 'Update', representing an incoming update from Telegram,
# and 'context' of type 'ContextTypes.DEFAULT_TYPE', which is a specific type used in the 'telegram.ext' library.

async def startcommand(update: Update, context: ContextTypes.DEFAULT_TYPE): # This function is typically used as the handler for a "/start" command in a Telegram bot. You can define the behavior of your bot when the "/start" command is invoked within this function.'update' provides information about the incoming message.'context' can be used to store and pass data between dfferent parts of your bot's conversation flow.
    await update.message.reply_text("Hello there.")

async def helpcommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How can I help you?")

async def waitcommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Wait!")
