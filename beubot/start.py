
import inspect
import sys

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from misc.colors import P, C
from misc.exporter import exporter

from .flows.genesis_flow import exec_genesis_new_user_flow
from .flows.prompts.nominal_prt import nominal_menu_prompt, nominal_rest_menu_prompt
p = P()
c = C()


async def start_hlr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"\nExec : {sys._getframe().f_code.co_name}")
    if not context.user_data:
        print(f"\n user data is none in context")
        await exec_genesis_new_user_flow(update, context)
    elif str(context.user_data['state']).__contains__('genesis'):
        # user is new with a clean user_data of
        # user is already in the process of creating a new account but has clicked on start again
        await exec_genesis_new_user_flow(update, context)
    else:
        print('User already has state')

        # check the role and direct to each of the appropriate functions handling that role
        state = context.user_data['state']
        role = context.user_data['role']
        print(f"\n state : {state}")
        print(f"\n role : {role}")
        if state == 'nominal':
            if role == 'general':
                await nominal_menu_prompt(update, context)
            elif role == 'restaurant':
                await nominal_rest_menu_prompt(update, context)
        else:
            print('state not nominal')
start_hlr.hlr = CommandHandler("start", start_hlr)


async def context_hlr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"\nExec : {sys._getframe().f_code.co_name}")

    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text=f"{str(context.bot_data)}",
        parse_mode=None)
    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text=f"{str(context.chat_data)}",parse_mode=None)
    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text=f"{str(context.user_data)}",parse_mode=None)
context_hlr.hlr = CommandHandler("context", context_hlr)


if __name__ != '__main__':
    __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()
