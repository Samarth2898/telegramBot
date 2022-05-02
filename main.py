from telegram.ext import Updater, CommandHandler,CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import logging

updater = Updater(token='5374655095:AAFXgm6THGMjWiF5SUJEa3SKVk7CIgtb8yU', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

list_of_users = [1238249576]

# writting functionality of the command
def start(update, context):
    message = 'Welcome to the bot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    keyboard = [[InlineKeyboardButton('Button: Print Clicked', callback_data=1)], ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    print("reply markup ", reply_markup)
    update.message.reply_text(text='Are you working today?', reply_markup=reply_markup)
    choice = update.callback_query.data
    print("this is the choice chosen",choice)


j = updater.job_queue

def once(context: CallbackContext):
    message = "Hey Samarth, Good morning!"
    
    # send message to all users
    for key in list_of_users:
        print("this is the key: ",key)
        id = key
        context.bot.send_message(chat_id=id, text=message)
        
        
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
j.run_once(once, 10)
updater.start_polling()
updater.idle()

