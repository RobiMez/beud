"""[AdminScope] commands are defined here"""
import sys, inspect
from telegram import Update 
from telegram.ext import ContextTypes , CommandHandler 
from misc.exporter import exporter

async def list_user_context_hlr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} \n{context.user_data}")

list_user_context_hlr.hlr = CommandHandler("ucontext", list_user_context_hlr)


if __name__ != '__main__':
    __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()