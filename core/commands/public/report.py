def init(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    bot.send_message(chat,"REPORT !",parse_mode='HTML')