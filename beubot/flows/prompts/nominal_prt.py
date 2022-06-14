from telegram import InlineKeyboardMarkup, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes

from ..keyboards.nominal_keyboards import nominal_r_menu, nominal_menu  



async def nominal_welcome_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardRemove()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"<b>🎉 Congrats on finishing your account setup,</b> <code>{update.effective_user.full_name}</code>\n"
        ),
        reply_markup=reply_markup)

async def nominal_menu_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dkeyboard = nominal_menu
    reply_markup = ReplyKeyboardMarkup(dkeyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"<b>Use the keyboard to place a new order.</b>\n"
        ),
        reply_markup=reply_markup)

async def nominal_rest_menu_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dkeyboard = nominal_r_menu
    reply_markup = ReplyKeyboardMarkup(dkeyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"<b>Use the keyboard to view pending orders.</b>\n"
        ),
        reply_markup=reply_markup)

# async def choose_rest_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     dkeyboard = make_restaurant_keyboard(update , context)
#     print(dkeyboard)
#     reply_markup = InlineKeyboardMarkup(dkeyboard)
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text=(
#             f"<b>Choose the restaurant.</b>\n"
#         ),
#         reply_markup=reply_markup)

# async def choose_food_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     dkeyboard = food_menu
#     print(dkeyboard)
#     reply_markup = InlineKeyboardMarkup(dkeyboard)
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text=(
#             f"<b>Choose the food.</b>\n"
#         ),
#         reply_markup=reply_markup)

# async def submission_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # dkeyboard = food_menu
#     ucon = context.user_data
#     # print(dkeyboard)
#     # reply_markup = InlineKeyboardMarkup(dkeyboard)
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text=(
#             f"<b>Placed an order for a {ucon['nominal_selected_food']} from {ucon['nominal_selected_restaurant']}.</b>\n"
#         ))

# async def send_order_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE , to_rest):
#     dkeyboard = make_accept_decline_keyboard(update , context , to_rest)
#     ucon = context.user_data
#     # print(dkeyboard)
#     # reply_markup = InlineKeyboardMarkup(dkeyboard)
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text=(
#             f"incoming order for [] from {to_rest}."
#         ))

