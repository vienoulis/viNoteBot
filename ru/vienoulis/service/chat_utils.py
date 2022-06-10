
# todo
def remove_msg_by(bot, chat_id, msg_id):
    try:
        bot.delete_message(chat_id=chat_id, message_id=msg_id)
    except Exception as error:
        print(f'Message_id does not exist: {error}')
