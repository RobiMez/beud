
# import inspect
# import sys
# from misc.exporter import exporter
# from misc.access_control import no_empty_ucontext
# from telegram.ext import MessageHandler, filters, CallbackQueryHandler
# from beubot.controllers.crud import users, orders

# from ..keyboards.nominal_keyboards import str_place_order, str_view_orders
# from ..keyboards.nominal_keyboards import str_r_view_orders 
# from beubot.scopes.general.flows.prompts.nominal_prt import choose_food_prompt, choose_rest_prompt
# from beubot.scopes.general.flows.prompts.nominal_prt import submission_prompt,send_order_confirmation

# @no_empty_ucontext
# async def place_order_hlr(update, context):
#     # starts the order placing flow
#     print('starting a new order')
#     await choose_rest_prompt(update, context)


# place_order_hlr.hlr = MessageHandler(
#     filters.Regex(str_place_order), place_order_hlr)
# # -------------------------------------------------------


# @no_empty_ucontext
# async def view_orders_hlr(update, context):
#     # starts the order placing flow
#     print('fetching all orders from this user')
#     pass


# view_orders_hlr.hlr = MessageHandler(
#     filters.Regex(str_view_orders), view_orders_hlr)
# # -------------------------------------------------------


# @no_empty_ucontext
# async def view_pending_orders_hlr(update, context):
#     # Starts the order placing flow
#     print('Fetching all pending orders for this restaurant')


# view_pending_orders_hlr.hlr = MessageHandler(
#     filters.Regex(str_r_view_orders), view_pending_orders_hlr)
# # -------------------------------------------------------

# # TODO: no time , fix if enough time 
# # @no_empty_ucontext
# # async def add_food_menu_hlr(update, context):
# #     # adds food to menu
# #     print('Adding a new food menu')
    
# #     # context.user_data['menu'].append(update.effective_message.text)


# # add_food_menu_hlr.hlr = MessageHandler(
# #     filters.Regex(str_r_add_menu), add_food_menu_hlr)
# # # -------------------------------------------------------


# @no_empty_ucontext
# async def restaurant_inline_hlr(update, context):
#     # starts the order placing flow
#     print('adding the restaurant as selected ')
#     context.user_data['nominal_selected_restaurant'] = update.callback_query.data.split('_')[
#         1]
#     # rest = await users.find_one({
#     #     "user_id": context.user_data['nominal_selected_restaurant']
#     # })
#     await choose_food_prompt(update, context)

# restaurant_inline_hlr.hlr = CallbackQueryHandler(
#     restaurant_inline_hlr, r'restaurant_')

# @no_empty_ucontext
# async def food_inline_hlr(update, context):
#     # starts the order placing flow
#     print('Adding the food as selected ')
#     context.user_data['nominal_selected_food'] = update.callback_query.data.split('_')[
#         1]
#     rest = orders.insert_one({
#         "user_id": context.user_data['user_id'],
#         "order_restaurant": context.user_data['nominal_selected_restaurant'],
#         "order_food": context.user_data['nominal_selected_food'],
#     })
#     await submission_prompt(update, context)
#     to_rest = context.user_data['nominal_selected_restaurant']
#     await send_order_confirmation(update, context , to_rest)

# food_inline_hlr.hlr = CallbackQueryHandler(
#     food_inline_hlr, r'food_')
# # -------------------------------------------------------


# if __name__ != '__main__':
#     __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()
