
import imp
import inspect
import sys
from beubot.flows.genesis_flow import genesis_persist
from misc.exporter import exporter
from misc.access_control import no_empty_ucontext

from telegram.ext import MessageHandler, filters
from ..keyboards.genesis_keyboards import  reg_restaurant_string, skip_futher_priv_string
from ..prompts.genesis_prt import prompt_genesis_role, prompt_phone_info
from ..prompts.genesis_prt import respond_to_delivery_state
from ..prompts.genesis_prt import respond_to_general_state
from ..prompts.genesis_prt import respond_to_restaurant_state


# @no_empty_ucontext
# async def del_staff_hlr(update, context):
#     context.user_data['role'] = 'delivery_staff'
#     context.user_data['orders'] = []
#     context.user_data['state'] = 'genesis:role'
#     await respond_to_delivery_state(update, context)
#     await genesis_persist(update, context)
    

# del_staff_hlr.hlr = MessageHandler(
#     filters.Regex(reg_delivery_string), del_staff_hlr)
# -------------------------------------------------------

@no_empty_ucontext
async def restaurant_hlr(update, context):
    context.user_data['role'] = 'restaurant'
    context.user_data['orders'] = []
    context.user_data['state'] = 'genesis:role'
    await respond_to_restaurant_state(update, context)
    await genesis_persist(update, context)
restaurant_hlr.hlr = MessageHandler(
    filters.Regex(reg_restaurant_string), restaurant_hlr)
# -------------------------------------------------------

@no_empty_ucontext
async def skip_role_hlr(update, context):
    context.user_data['role'] = 'general'
    context.user_data['state'] = 'genesis:role'
    context.user_data['orders'] = []
    await respond_to_general_state(update, context)
    await genesis_persist(update, context)


skip_role_hlr.hlr = MessageHandler(
    filters.Regex(skip_futher_priv_string), skip_role_hlr)
# -------------------------------------------------------

@no_empty_ucontext
async def sent_phone_number_hlr(update, context):
    context.user_data['phone_number'] = update.effective_message.contact.phone_number
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"💾 Saved Phone Number: {context.user_data['phone_number']}",
    )
    context.user_data['state'] = 'genesis:personal_data:phone_number'
    await prompt_genesis_role(update, context)
sent_phone_number_hlr.hlr = MessageHandler(
    filters.CONTACT, sent_phone_number_hlr)
# -------------------------------------------------------


if __name__ != '__main__':
    __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()
