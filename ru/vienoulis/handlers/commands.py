from telebot import types

from ru.vienoulis.main import bot


@bot.message_handler(commands=['start'])
def start(msg):
    print('start.enter;')
    keyboard = types.InlineKeyboardMarkup()
    test_key = types.InlineKeyboardButton(text='Test', callback_data='test')
    clear_kay = types.InlineKeyboardButton(text='Clear', callback_data='clear')
    keyboard.add(test_key, clear_kay)
    bot.send_message(chat_id=msg.chat.id, text='Hello app was started', reply_markup=keyboard)
    print('start.end;')


@bot.message_handler(commands=['clear'])
def clear(message):
    print('clear.enter;')
    new_message_id = message.message_id
    while new_message_id > 1:
        try:
            bot.delete_message(chat_id=message.chat.id, message_id=new_message_id)
        except Exception as error:
            print(f'Message_id does not exist: {new_message_id} - {error}')
        new_message_id = new_message_id - 1

    start(message)
    print('clear.end;')
