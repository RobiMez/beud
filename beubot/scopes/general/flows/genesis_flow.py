"""Deals with the genesis [ account creation and privillage ] choice flow """

from ....controllers.crud import users

# steps to clear and sync genesis flow :
    # genesis:telegram_data
    # genesis:personal_data
    # genesis:personal_data:phone_number
    # genesis:role
    # genesis:persist

import sys
from telegram.ext import ContextTypes, CommandHandler
from telegram import Update
from .prompts.genesis_prt import prompt_genesis_role , genesis_welcome_and_onboarding, prompt_phone_info


async def genesis_init(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Initial step : scrapes data from the telegram user and asks for user role"""
    # Genesis init starts off with a clean slate
    context.user_data.clear()
    # these things get exported at sync to mongodb so we gonna pick them off the update
    context.user_data['full_name'] = update.effective_user.full_name
    context.user_data['username'] = update.effective_user.username
    context.user_data['user_id'] = update.effective_user.id
    # setting the state to genesis:telegram_data to avoid it going to other flows 
    context.user_data['state'] = 'genesis:telegram_data'
    # send the onboarding text and keyboard
    await genesis_welcome_and_onboarding(update, context)


async def genesis_role(update, context):
    """User asked to choose a role"""
    print(f"\nExec : {sys._getframe().f_code.co_name}")
    await prompt_genesis_role(update, context) #prompts for phone 


async def genesis_data(update, context):
    """User asked for personal data"""
    print(f"\nExec : {sys._getframe().f_code.co_name}")
    await prompt_phone_info(update, context)


async def genesis_persist(update, context):
    """Step where user is added to the mongo db"""
    print(f"\nExec : {sys._getframe().f_code.co_name}")
    if not users.find_one({'telegram_id': update.effective_user.id}):
        print('Persisting genesis data ')
        users.insert_one(context.user_data)
        # set state away from genesis to avoid doing the setup again 
        context.user_data['state'] = 'nominal'


def genesis_nuke_and_recreate(update, context):
    """delete users incomplete data from db then proceed to genesis_flow_new_user"""
    print(f"\nExec : {sys._getframe().f_code.co_name}")
    if users.find_one({'telegram_id': update.effective_user.id}):
        print('exec nuke ')
        users.find_one_and_delete({'telegram_id': update.effective_user.id})
    


async def exec_genesis_new_user_flow(update, context):
    """Execute the genesis flow for a new user"""
    print(f"\nExec : {sys._getframe().f_code.co_name}")

    # new user so clears db of possible entries 
    genesis_nuke_and_recreate(update, context) 
    # initializes the ucontext with the telegram data 
    await genesis_init(update,context)
    # gets general common scope info for user , rest and disp 
    await genesis_data(update, context)
    # gets the user role and prompt-handles the additional data the role needs 

