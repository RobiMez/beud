
import json

import inspect
import sys

from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from misc.colors import P, C
from misc.exporter import exporter

from beubot.models.user import User
from beubot.controllers.crud import users, rests, orders
from beubot.keyboards.startkbd import start_keyboard

p = P()
c = C()


async def start_hlr(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # state management 



    if not context.user_data['current_state']:

        context.user_data['name'] = update.effective_chat.first_name
        context.user_data['username'] = update.effective_chat.username
        context.user_data['last_exec'] = sys._getframe().f_code.co_name
        context.user_data['current_state'] = 'genesis:command'

        # add user to the database as a regular user if he/she is not in the database

        # create an instance of user class
        user = User(update.effective_user.id, update.effective_chat.id)

        # add it to database if it doesn't already exist
        if not users.find_one({'telegram_id': user.telegram_id}):
            p.o(c.green, 'Adding user to database...', bold=True)
            # execute insert operation
            users.insert_one(user.__dict__)
            # set states to reflect as such
            context.user_data['current_state'] = 'genesis:database'
        else:
            p.o(c.b_black, 'User already exists in database...', bold=True)

        # send welcome message and a reply keyboard based on state equalling genesis

        custom_keyboard = start_keyboard
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        # TODO: make messages templatable based on state 
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                f"<b>Hi there,</b> <code>{update.effective_chat.first_name}</code> Welcome to your account setup.\n"
                f"<i>You are Currently registered as a general user of BeuBot.</i>\n\n"
                f"If you are a <b>Restaurant</b> \n\tPlease click on register as restaurant.\n"
                f"If you are a <b>Delivery staff</b> \n\tPlease click on register as delivery.\n"
                f"Otherwise you can click on Skip to proceed.\n"

                "\n\n Here is some Debug info "
                f"\n {context.bot_data}\n {context.user_data}\n {context.chat_data}"),
            reply_markup=reply_markup)

    elif context.user_data['current_state'] == 'genesis:database':
        
        custom_keyboard = start_keyboard
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                f"<b>Hi there,</b> <code>{update.effective_chat.first_name}</code> Welcome to your account setup.\n"
                f"<i>You are Currently registered as a general user of BeuBot.</i>\n\n"
                f"If you are a <b>Restaurant</b> \n\tPlease click on register as restaurant.\n"
                f"If you are a <b>Delivery staff</b> \n\tPlease click on register as delivery.\n"
                f"Otherwise you can click on Skip to proceed.\n"

                "\n\n Here is some Debug info "
                f"\n {context.bot_data}\n {context.user_data}\n {context.chat_data}"),
            reply_markup=reply_markup)
        
start_hlr.hlr = CommandHandler("start", start_hlr)


if __name__ != '__main__':
    __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()
