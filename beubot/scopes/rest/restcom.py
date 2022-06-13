"""[RestScope] commands are defined here"""
import sys
from telegram import Update
from telegram.ext import ContextTypes


async def accept_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def reject_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def list_pending_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def dispatch_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def ban_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def unban_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def set_working_hours(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def set_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def set_is_currently_open(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def clear_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def add_meal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")


async def remove_meal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    func_name = sys._getframe().f_code.co_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{update.effective_chat.first_name} {func_name} ")

