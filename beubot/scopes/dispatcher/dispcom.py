"""[DispatcherScope][DelivererScope] commands are defined here"""
import sys
from telegram import Update
from telegram.ext import ContextTypes


async def order_delivered(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def order_on_the_way(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def order_damaged(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")
