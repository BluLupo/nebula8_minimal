def check_status(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    user = update.effective_message.from_user
    if user.username is None or "":
        msg = "#Automatic Handler\n<code>{}</code> set a username! You were kicked for safety!".format(user.id)
        bot.send_message(chat,msg,parse_mode='HTML')