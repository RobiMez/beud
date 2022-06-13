
import json

import inspect
import sys

from telegram import  ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from misc.colors import P, C
from misc.exporter import exporter

from beubot.models.user import User
from beubot.controllers.crud import users, rests, orders

p = P()
c = C()

async def start_hlr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    context.user_data['name'] = update.effective_chat.first_name
    context.user_data['username'] = update.effective_chat.username
    context.user_data['last_exec'] = sys._getframe().f_code.co_name
    context.user_data['current_state'] = 'genesis'
    

    # add user to the database as a regular user if he/she is not in the database
    
    # create an instance of user class
    user = User(update.effective_user.id, update.effective_chat.id)
    
    # add it to database if it doesn't already exist
    if not users.find_one({'telegram_id': user.telegram_id}):
        p.o(c.green, 'Adding user to database...', bold=True)
        # execute insert operation
        users.insert_one(user.__dict__)
        # set states to reflect as such 
        context.user_data['current_state'] = 'database_entry_added'
    else :
        p.o(c.b_black, 'User already exists in database...', bold=True)

    # send welcome message and a reply keyboard

    custom_keyboard = [
        ['top-left', 'top-right'],
        ['bottom-left', 'bottom-right']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"<b>Hi</b> <code>{update.effective_chat.first_name}</code> Im already awake. here is some junk"
            f"\n {context.bot_data}\n {context.user_data}\n {context.chat_data}"),
        reply_markup=reply_markup)

start_hlr.hlr = CommandHandler("start", start_hlr)


if __name__ != '__main__':
    __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()
