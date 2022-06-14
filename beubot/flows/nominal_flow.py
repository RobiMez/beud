# """Deals with the nominal [ normal account functionality ] flows """

# import sys
# from telegram.ext import ContextTypes, CommandHandler
# from telegram import Update
# from ....controllers.crud import users


# # nominal flows : [general context]

# async def nominal_show_menu(update, context):
#     pass


# # nominal:place_order
# # push order to db as draft (non-submit) when finished placing
# async def nominal_place_order(update, context):
#     print(f"\nExec : {sys._getframe().f_code.co_name}")

# # nominal:view_orders
# # refetch orders from db before viewing


# async def nominal_view_orders(update, context):
#     print(f"\nExec : {sys._getframe().f_code.co_name}")

# # nominal:cancel_order
# # delete order from db and update restaurants affected


# async def nominal_cancel_order(update, context):
#     print(f"\nExec : {sys._getframe().f_code.co_name}")

# # nominal:submit_order
# # push order to db and notify restaurant


# async def nominal_submit_order(update, context):
#     print(f"\nExec : {sys._getframe().f_code.co_name}")
# # nominal:recieved_order
# # update order status to recieved


# async def nominal_recieved_order(update, context):
#     print(f"\nExec : {sys._getframe().f_code.co_name}")
# # nominal:rate
# # update rating fields of restaurant


# async def nominal_rate(update, context):
#     print(f"\nExec : {sys._getframe().f_code.co_name}")
