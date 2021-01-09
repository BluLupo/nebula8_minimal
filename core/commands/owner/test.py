def init(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    bot.send_message(chat,"OWNER !",parse_mode='HTML')