"""[GeneralScope][UserScope] commands are defined here"""

import sys
import inspect
import sys

from misc.exporter import exporter

from beubot.controllers.crud import users, rests, orders
from beubot.keyboards.startkbd import start_keyboard


from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import  ContextTypes, CommandHandler

async def register_as_restaurant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def register_as_dispatcher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def register_for_vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def place_asap_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def place_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def cancel_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def submit_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def list_placed_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def order_recieved(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")





if __name__ != '__main__':
    __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()
