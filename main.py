""" Main script """

import os
import logging
from logging import handlers
from time import perf_counter

from misc.colors import P , C 
# telegram api imports 
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Defaults
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler





from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.beubot
# database definitions
users = db['users']
rests = db['restaurants']
orders = db['orders']

# -- local imports [ breaking up this file ] -- #
from beubot.scopes.general.usercom import *
from beubot.scopes.rest.restcom import *
from beubot.scopes.admin.admincom import *
from beubot.scopes.dispatcher.dispcom import *
# -- local imports [ breaking up this file ] -- #


# make directory if not exists 
if not os.path.exists('./logs'):
    os.makedirs('./logs')

# logging configuration 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
    handlers=[
        handlers.TimedRotatingFileHandler(
            './logs/debug.log', encoding='utf-8', when='midnight'),
        logging.StreamHandler()
    ]
)
# colored print initializations 
p = P()
c = C()
# perfcounter initial execution time 
st = perf_counter()
# _____________________ Functionality _____________________________



def main():
    defaults = Defaults(parse_mode=ParseMode.HTML)
    d = ApplicationBuilder().token('5564359967:AAEBs6ntRLskO30isnHey8yEzcizFz2HmCc').defaults(defaults).build()
    handlers = [

        
        ,CommandHandler('accept_order', accept_order)
        ,CommandHandler('reject_order', reject_order)
        ,CommandHandler('list_restaurant_orders', list_pending_orders)
        ,CommandHandler('dispatch_order', dispatch_order)
        ,CommandHandler('ban_user', ban_user)
        ,CommandHandler('unban_user', unban_user)
        ,CommandHandler('set_working_hours', set_working_hours)
        ,CommandHandler('set_location', set_location)
        ,CommandHandler('set_is_currently_open', set_is_currently_open)
        ,CommandHandler('clear_menu', clear_menu)
        ,CommandHandler('add_meal', add_meal)
        ,CommandHandler('remove_meal', remove_meal)
        
        ,CommandHandler('order_delivered', order_delivered)
        ,CommandHandler('order_on_the_way', order_on_the_way)
        ,CommandHandler('order_damaged', order_damaged)
    ]
    
    for handler in handlers:
        d.add_handler(handler)
        
    p.o(c.green,
        f"🔥 Started polling for updates in {str(round(st-perf_counter() , 2))[1:]} Secs." , 
        bold=True)
    d.run_polling()
    p.o(c.purple,
        f"💀 Program ended after a runtime of {str(round(st-perf_counter() , 2))[1:]} Secs." , 
        bold=True)
# _____________________ Functionality _____________________________

if __name__ == '__main__':
    main()