from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import logging
from telegram.bot import Bot

updater = Updater(token='5374655095:AAFXgm6THGMjWiF5SUJEa3SKVk7CIgtb8yU', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

list_of_users = [1238249576]

# writting functionality of the command
def start(update, context):
    message = 'Welcome to the bot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)



def once(context: CallbackContext):
    message = "Hey Samarth, Good morning!"
    
    # send message to all users
    for key in list_of_users:
        print("this is the key: ",key)
        id = key
        context.bot.send_message(chat_id=id, text=message)
        keyboard = [[InlineKeyboardButton("Yes! Iam working", callback_data='1'),
                 InlineKeyboardButton("No, I'll be on leave today!", callback_data='2')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=id, text='Are you working today', reply_markup=reply_markup)

def c_back_respons(update: Update, context: CallbackContext):
    id = list_of_users[0]
    call_back_data = update.callback_query.data
    if call_back_data in ("1"):
        update.callback_query.edit_message_reply_markup(None)
        keyboard = [[InlineKeyboardButton("Working from office!", callback_data='3'),
                 InlineKeyboardButton("Working from home!", callback_data='4')]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=id, text='Great! Are you working from office or home??', reply_markup=reply_markup)
    if call_back_data in ("2"):
        print("option 2 selected")
    if call_back_data in ("3"):
        update.callback_query.edit_message_reply_markup(None)
        context.bot.send_message(chat_id=id, text='What are you working on? Type in your answer!')
        
        
j = updater.job_queue       
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CallbackQueryHandler(c_back_respons))
j.run_once(once, 10)
updater.start_polling()
updater.idle()

