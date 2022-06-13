""" Main script """

from beubot.start import __handlers__ as start_hlr
import os
import logging
from logging import handlers as lhand
from time import perf_counter

from setuptools import Command

from misc.colors import P, C
# telegram api imports
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Defaults, PicklePersistence , filters
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler , MessageHandler




# -- local imports [ breaking up this file ] -- #
# from beubot.scopes.general.usercom import handlers as gen_user_hlr
# from beubot.scopes.rest.restcom import handlers as restcom_hlr
# from beubot.scopes.admin.admincom import admincom_hlr
# from beubot.scopes.dispatcher.dispcom import dispcom_hlr
# -- local imports [ breaking up this file ] -- #


# make directory if not exists
if not os.path.exists('./logs'):
    os.makedirs('./logs')

# logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
    handlers=[
        lhand.TimedRotatingFileHandler(
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


async def error_handler(update: Update, context):
    p.o(c.red, context.error)
    p.o(c.orange, update)
    p.o(c.yellow, context)

async def general_hlr(update: Update, context):
    p.o(c.b_black, context)
    p.o(c.b_black, update)


def main():
    defaults = Defaults(parse_mode=ParseMode.HTML)
    persistence = PicklePersistence('Persistence')
    d = ApplicationBuilder().token('5564359967:AAEBs6ntRLskO30isnHey8yEzcizFz2HmCc').defaults(
        defaults).persistence(persistence).build()

    handlers = []
    # parse handlers from the import and add them to be linked
    for handler in start_hlr:
        handlers.append(handler)
    # link the handlers to the bot
    for handler in handlers:
        d.add_handler(handler)

    d.add_error_handler(error_handler)
    globalhlr = MessageHandler(filters.ALL, general_hlr)
    d.add_handler(globalhlr)
    p.o(c.green,
        f"🔥 Started polling for updates in {str(round(st-perf_counter() , 2))[1:]} Secs.",
        bold=True)
    # make this a webhook in production
    d.run_polling()
    p.o(c.purple,
        f"💀 Program ended after a runtime of {str(round(st-perf_counter() , 2))[1:]} Secs.",
        bold=True)
# _____________________ Functionality _____________________________


if __name__ == '__main__':
    main()