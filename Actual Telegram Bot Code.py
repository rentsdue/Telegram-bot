from typing import Final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ContextTypes, Application

# Token: Define a constant variable 'TOKEN' with the Telegram Bot API token as its value.
TOKEN: Final = '6430569246:AAHOqlsBSKvrAV0wbun5pzXdNlmZUgOO1KY'  # Replace with your actual bot token

#Username: Define a constant variable 'BOT_USERNAME' with the bot's username as its value.
BOT_USERNAME: Final = '@Thebotsonbot'

#Commands: Define an asynchronous function 'startcommand' that takes two arguments: 'update' of type 'Update', representing an incoming update from Telegram, and 'context' of type 'ContextTypes.DEFAULT_TYPE', which is a specific type used in the 'telegram.ext' library.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): # This function is typically used as the handler for a "/start" command in a Telegram bot. You can define the behavior of your bot when the "/start" command is invoked within this function.'update' provides information about the incoming message.'context' can be used to store and pass data between dfferent parts of your bot's conversation flow.
    await update.message.reply_text("Hello there. How can I help you?")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a bot. How can I help you?")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a telegram bot designed to respond to basic commands. I can respond uniquely to a wide range of prompts!")

async def sentencereverse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please send me a message, and I'll reverse the words in it.")
    if update.message and update.message.text:
        user_message = update.message.text #Defines variable user_message
        words = user_message.split() #Turns variable into words
        reversed_message = ' '.join(reversed(words)) #Reverses the words, ''.join ensures a space between the words
        await update.message.reply_text(f"Reversed message: {reversed_message}") #Displays the reversed message
    else:
        await update.message.reply_text("Try again!")

async def wordreverse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please send a single word and I'll reverse it!")
    if update.message and update.message.text:
        user_message=update.message.text
        words = user_message.split()
        if len(words)>1:
            await update.message.reply_text("Please input a single word only!")
        else:
            reversed_word = words[0][::-1]
            update.message.reply_text(f"Reversed word: {reversed_word}")
#Define app:
app=Application.builder().token(TOKEN).build() 

# Add command handlers
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help))
app.add_handler(CommandHandler('about', about))
app.add_handler(CommandHandler('sentencereverse', sentencereverse))
app.add_handler(CommandHandler('wordreverse', wordreverse))

#Responses
def responsehandling (text: str)->str:
    usermessage: str=text.lower()
    if "hello" in usermessage:
        return "Hello there."
    elif "how are you" in usermessage:
        return "I'm doing fine, thank you very much for asking."
    elif "thank" in usermessage:
        return "You're welcome! I'm just doing my job!"
    elif "sorry" in usermessage:
        return "It's alright!"

#Respond handlers
app.add_handler(MessageHandler(filters.TEXT, responsehandling))