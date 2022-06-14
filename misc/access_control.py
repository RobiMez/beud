from functools import wraps



def no_empty_ucontext(func):
    @wraps(func)
    async def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if not context.user_data:
            print(f"Unauthorized : Access denied for {user_id} .")
            await context.bot.send_message(
                chat_id = update.effective_chat.id,
                text = "🚫 Access denied. Please press /start.",)
            return
        return await func(update, context, *args, **kwargs)
    return wrapped