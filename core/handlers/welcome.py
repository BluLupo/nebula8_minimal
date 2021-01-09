def init(update,context):
    for member in update.message.new_chat_members:
        update.message.reply_text("{username} add group".format(username=member.username))