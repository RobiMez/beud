
from cgitb import handler
import inspect
from re import I
import sys
from typing import Union, List

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler,MessageHandler
from misc.colors import P,C

from misc.exporter import exporter


def build_menu(
    buttons: List[InlineKeyboardButton],
    n_cols: int,
    header_buttons: Union[InlineKeyboardButton, List[InlineKeyboardButton]] = None,
    footer_buttons: Union[InlineKeyboardButton,
                          List[InlineKeyboardButton]] = None
) -> List[List[InlineKeyboardButton]]:

    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons if isinstance(
            header_buttons, list) else [header_buttons])
    if footer_buttons:
        menu.append(footer_buttons if isinstance(
            footer_buttons, list) else [footer_buttons])
    return menu


async def start_hlr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    context.user_data['name'] = update.effective_chat.first_name

    custom_keyboard = [['top-left', 'top-right'], 
                    ['bottom-left', 'bottom-right']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"Hi {update.effective_chat.first_name} Im already awake. here is some junk"
            f"\n {context.bot_data}\n {context.user_data}\n {context.chat_data}"),
        reply_markup=reply_markup)

start_hlr.hlr = CommandHandler("start", start_hlr)


if __name__ != '__main__':

    __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()