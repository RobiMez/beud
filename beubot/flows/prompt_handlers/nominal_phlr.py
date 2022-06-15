
from cgitb import text
import inspect
import sys

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from misc.exporter import exporter
from misc.access_control import no_empty_ucontext
from telegram.ext import MessageHandler, filters, CallbackQueryHandler
# from beubot.controllers.crud import users, orders

from ..keyboards.nominal_keyboards import str_place_order
from ..keyboards.nominal_keyboards import str_r_view_orders , str_r_view_accepted_orders
from beubot.flows.prompts.nominal_prt import choose_rest_prompt


@no_empty_ucontext
async def place_order_hlr(update, context):
    # starts the order placing flow
    print('starting a new order')
    await choose_rest_prompt(update, context)


place_order_hlr.hlr = MessageHandler(
    filters.Regex(str_place_order), place_order_hlr)
# # -------------------------------------------------------


# @no_empty_ucontext
# async def view_orders_hlr(update, context):
#     # starts the order placing flow
#     print('fetching all orders from this user')
#     pass


# view_orders_hlr.hlr = MessageHandler(
#     filters.Regex(str_view_orders), view_orders_hlr)
# # -------------------------------------------------------


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


@no_empty_ucontext
async def restaurant_inline_hlr(update, context):
    # starts the order placing flow
    print('adding the restaurant as selected ')
    print(update.callback_query.data)
    context.user_data['selected_restaurant'] = update.callback_query.data.split('_')[
        1]
    selected_resturant = context.bot_data[
        int(update.callback_query.data.split('_')[1])]
    menu = selected_resturant['menu']
    print('Selected Restaurant: ', selected_resturant)
    menukbd = []
    for food in menu:
        menukbd.append([InlineKeyboardButton(
            food, callback_data="food_" + food)])
    reply_markup = InlineKeyboardMarkup(menukbd)
    await context.user_data['message'].delete()
    await context.bot.send_message(
        chat_id=update.callback_query.message.chat_id,
        text='💾 Selected Restaurant : <b>' +
        selected_resturant['full_name'] +
        "\n</b> Please choose the food you want to order.",
        reply_markup=reply_markup)

restaurant_inline_hlr.hlr = CallbackQueryHandler(
    restaurant_inline_hlr, r'restaurant_')


@no_empty_ucontext
async def food_inline_hlr(update, context):
    # starts the order placing flow
    print('Adding the food as selected ')
    food_selected = update.callback_query.data.split('_')[1]
    context.user_data['selected_food'] = food_selected

    for_rest = context.user_data['selected_restaurant']
    print(for_rest)
    print(food_selected)

    context.bot_data[int(for_rest)]['orders'].append(
        {
            'food': food_selected,
            'status': 'pending',
            'from_id': update.callback_query.from_user.id,
            'from_user': update.callback_query.from_user,
        }
    )
    await context.bot.send_message(
        text='✨ New order incoming from<b> ' +
        update.callback_query.from_user.username + '</b> for <i><b>' + food_selected+ '</b></i>',
        chat_id=int(for_rest)) 
    await context.bot.send_message(
        chat_id=update.callback_query.message.chat_id,
        text=f'🎉 An order for <b>{food_selected}</b> added successfully')
    # rest = orders.insert_one({
    #     "user_id": context.user_data['user_id'],
    #     "order_restaurant": context.user_data['nominal_selected_restaurant'],
    #     "order_food": context.user_data['nominal_selected_food'],
    # })

    # await submission_prompt(update, context)
    # to_rest = context.user_data['nominal_selected_restaurant']
    # await send_order_confirmation(update, context , to_rest)

food_inline_hlr.hlr = CallbackQueryHandler(
    food_inline_hlr, r'food_')
# # -------------------------------------------------------


@no_empty_ucontext
async def accept_hlr(update, context):
    # starts the order placing flow
    print(f'accepting the order {update.callback_query.data}')
    orders = context.bot_data[int(update.effective_user.id)]['orders']
    for order in orders:
        print(order)
        if order['from_id'] == int(update.callback_query.data.split('_')[2]):
            if order['food'] == update.callback_query.data.split('_')[1]:
                order['status'] = 'accepted'
                await order['message'].delete()
                await context.bot.send_message(chat_id=update.effective_user.id, text='Order accepted')
                await context.bot.send_message(chat_id=int(order['from_id']), text=f'Order {order["food"]} has been accepted and will be prepared soon')

accept_hlr.hlr = CallbackQueryHandler(
    accept_hlr, r'accept_')
# # -------------------------------------------------------

@no_empty_ucontext
async def prepare_hlr(update, context):
    # starts the order placing flow
    print(f'accepting the order {update.callback_query.data}')
    orders = context.bot_data[int(update.effective_user.id)]['orders']
    for order in orders:
        print(order)
        if order['from_id'] == int(update.callback_query.data.split('_')[2]):
            if order['food'] == update.callback_query.data.split('_')[1]:
                order['status'] = 'prepared'
                # await order['message'].delete()
                await context.bot.send_message(chat_id=update.effective_user.id, text='Order marked as prepared')
                await update.callback_query.message.delete()
                await context.bot.send_message(chat_id=int(order['from_id']), text=f'Your order for<b> {order["food"]}</b> has been marked as prepared')

prepare_hlr.hlr = CallbackQueryHandler(
    prepare_hlr, r'prepare_')
# # -------------------------------------------------------


@no_empty_ucontext
async def reject_hlr(update, context):
    # starts the order placing flow
    print(f'rejecting the order {update.callback_query.data}')
    orders = context.bot_data[int(update.effective_user.id)]['orders']
    for order in orders:
        if order['from_id'] == int(update.callback_query.data.split('_')[2]):
            if order['food'] == update.callback_query.data.split('_')[1]:
                context.bot_data[
                    int(update.effective_user.id)]['orders'].remove(order)
                # await order['message'].delete()
                await update.callback_query.message.delete()
                await context.bot.send_message(chat_id=update.effective_user.id, text='Order rejected')
                await context.bot.send_message(chat_id=int(order['from_id']), text=f'Sorry but your order for <b>{order["food"]}</b> has been rejected.')
reject_hlr.hlr = CallbackQueryHandler(
    reject_hlr, r'reject_')


@no_empty_ucontext
async def view_pending_orders_hlr(update, context):
    # Starts the order placing flow
    print('Fetching all pending orders for this restaurant')
    orders = context.bot_data[update.effective_user.id]['orders']
    no_pending_orders = True
    if orders :
        for order in orders:
            if not order['status'] in ['accepted', 'prepared']:
                no_pending_orders = False
                keyboard = [
                    [
                        InlineKeyboardButton(
                            '✅ Accept', callback_data="accept_" + order['food']+'_'+str(order['from_id'])),
                        InlineKeyboardButton(
                            '❌ Reject', callback_data="reject_" + order['food']+'_'+str(order['from_id']))]
                ]
                text = f"Order for <b><i>{order['food']}</i></b> from user <b>{str(context.bot_data[int(order['from_id'])]['full_name'])}</b>\nStatus: <code>{order['status'].capitalize()}</code>"
                message = await context.bot.send_message(
                    chat_id=update.effective_user.id,
                    text=text,
                    reply_markup=InlineKeyboardMarkup(keyboard))
                order['message'] = message
    else:
        message = await context.bot.send_message(
                chat_id=update.effective_user.id,
                text='There are <b>no pending orders</b> for your restaurant at the moment. \n\n🏖 Chill back and wait until a user orders food from your restaurant.',
                )
    if no_pending_orders:
        message = await context.bot.send_message(
                chat_id=update.effective_user.id,
                text='There are <b>no pending orders</b> for your restaurant at the moment. \n\n🏖 Chill back and wait until a user orders food from your restaurant.',)
        
view_pending_orders_hlr.hlr = MessageHandler(
    filters.Regex(str_r_view_orders), view_pending_orders_hlr)

@no_empty_ucontext
async def view_accepted_orders_hlr(update, context):
    # Starts the order placing flow
    print('Fetching all accepted orders for this restaurant')
    orders = context.bot_data[update.effective_user.id]['orders']
    no_accepts_flag = True
    
    for order in orders:
        if order['status'] == 'accepted':
            no_accepts_flag = False
            keyboard = [
                [
                    InlineKeyboardButton(
                        'Mark Prepared', callback_data="prepare_" + order['food']+'_'+str(order['from_id'])),
                    InlineKeyboardButton(
                        'Reject', callback_data="reject_" + order['food']+'_'+str(order['from_id']))]
            ]
            text = f"Order for <b><i>{order['food']}</i></b> from user <b>{str(context.bot_data[int(order['from_id'])]['full_name'])}</b><code> in Queue</code>"
            await context.bot.send_message(
                chat_id=update.effective_user.id,
                text=text,
                reply_markup=InlineKeyboardMarkup(keyboard))
    if no_accepts_flag:
        
        message = await context.bot.send_message(
            chat_id=update.effective_user.id,
            text='There are <b>no accepted orders</b> for your restaurant at the moment.\n\nOrders that get accepted can be marked as prepared here. ',
            )


view_accepted_orders_hlr.hlr = MessageHandler(
    filters.Regex(str_r_view_accepted_orders), view_accepted_orders_hlr)


if __name__ != '__main__':
    __handlers__ = exporter(inspect.getmembers(sys.modules[__name__])).export()
