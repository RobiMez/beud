
import inspect
import sys

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from misc.colors import P, C
from misc.exporter import exporter

from .flows.genesis_flow import exec_genesis_new_user_flow

p = P()
c = C()


async def start_hlr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"\nExec : {sys._getframe().f_code.co_name}")
    if not context.user_data == None or str(context.user_data['state']).__contains__('genesis'):
        # user is new with a clean user_data of  
        # user is already in the process of creating a new account but has clicked on start again
        await exec_genesis_new_user_flow(update, context)
    else:
        print('User already has state')

start_hlr.hlr = CommandHandler("start", start_hlr)


if __name__ != '__main__':
    __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()
