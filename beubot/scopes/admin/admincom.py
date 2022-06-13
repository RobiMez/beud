"""[AdminScope] commands are defined here"""
import sys
from telegram import Update
from telegram.ext import ContextTypes


async def wipe_db(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")
