from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from ...keyboards.startkbd import dstaff_keyboard, start_keyboard

# welcome message for the user


async def genesis_welcome_and_onboarding(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dkeyboard = start_keyboard
    reply_markup = ReplyKeyboardMarkup(dkeyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"<b>Hi there,</b> <code>{update.effective_user.full_name}</code>\n"
            "<b>Welcome to your BeuDeliveries account setup.</b>\n "
            "<i>This is a one time setup so take your time and enter values correctly.</i>\n"

        ),
        reply_markup=reply_markup)


async def prompt_genesis_role(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dkeyboard = start_keyboard
    reply_markup = ReplyKeyboardMarkup(dkeyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"<i>You Currently are a normal user of BeuBot.</i>\n\n"

            f"If you are a <b>Restaurant manager</b> \n\tPlease click on Restaurant.\n"
            f"\nIf you are a <b>Delivery staff</b> \n\tPlease click on Delivery staff.\n"
            f"\nOtherwise you can click on Skip to proceed with the rest of the setup.\n"),
        reply_markup=reply_markup)


async def prompt_phone_info(update, context):
    dkeyboard = dstaff_keyboard
    reply_markup = ReplyKeyboardMarkup(dkeyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"\nLets start with your Phone Number.\n\n"),
        reply_markup=reply_markup)


async def respond_to_restaurant_state(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"\nPerfect , you have been granted additional commands as a <b>restaurant</b>.\n\n"),
    )


async def respond_to_general_state(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"\nPerfect , That's all for now.\n\n"),
    )


async def respond_to_delivery_state(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"\nPerfect , You have been granted additional commands as a <b>Delivery staff</b>.\n\n"),
    )
