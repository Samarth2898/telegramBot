from telegram.ext import Updater, CommandHandler
import logging

updater = Updater(token='5374655095:AAFXgm6THGMjWiF5SUJEa3SKVk7CIgtb8yU', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# writting functionality of the command
def start(update, context):
    message = 'Welcome to the bot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
# give a name to the command and add it to the dispaatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling() # enable bot to get updates