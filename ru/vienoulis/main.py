from telebot import *
from data.orm import add_title_orm, get_all_title, remove_title_by_id, get_title_by_id
from ru.vienoulis.service.chat_utils import remove_msg_by
from ru.vienoulis.service.keybords import get_started_kbrd, get_list_kbrd_from
from utils.const.buttoms import *

bot = telebot.TeleBot('855393784:AAGxBrLMZoVjzcWv6veIh2YyhQdt5UmfX6o')


@bot.message_handler(commands=['start'])
def start(msg):
    print('start.enter;')
    bot.send_message(chat_id=msg.chat.id, text='Hello app was started', reply_markup=get_started_kbrd())
    remove_msg_by(bot, chat_id=msg.chat.id, msg_id=msg.message_id)
    print('start.end;')


@bot.callback_query_handler(func=lambda message: message.data == CLEAR_BTN.callback_data)
def clear_kay(msg):
    print('clear_kay.enter;')
    new_message_id = msg.message.message_id
    # bot.delete_message(chat_id=message.message.chat.id, message_id=263)

    while new_message_id > 1:
        try:
            bot.delete_message(chat_id=msg.message.chat.id, message_id=new_message_id)
        except Exception as error:
            print(f'Message_id does not exist: {new_message_id} - {error}')
        new_message_id = new_message_id - 1
    remove_msg_by(bot, chat_id=msg.message.chat.id, msg_id=msg.message.message_id)
    print('clear_kay.end;')


@bot.callback_query_handler(func=lambda message: message.data == SHOW_TITLES_LIST_BTN.callback_data)
def show_titles_btn(msg):
    print('show_title_btn.enter;')
    keyboard = get_list_kbrd_from(elements=get_all_title(), prefix='title_')
    bot.send_message(chat_id=msg.message.chat.id, text='Titles: ', reply_markup=keyboard)

    remove_msg_by(bot, chat_id=msg.message.chat.id, msg_id=msg.message.message_id)
    print('show_title_btn.end;')


@bot.callback_query_handler(func=lambda c: c.data.startswith('title_'))
def show_title_by_id(msg):
    print('show_title_by_id.enter;', msg.data)
    title_id = int(str(msg.data).removeprefix('title_'))
    title = get_title_by_id(title_id)


    bot.send_message(chat_id=msg.message.chat.id, text=title.name, reply_markup=get_started_kbrd())
    remove_msg_by(bot, chat_id=msg.message.chat.id, msg_id=msg.message.message_id)
    print('show_title_by_id.end;')


@bot.message_handler(commands=['clear'])
def clear(msg):
    print('clear.enter;')
    new_message_id = msg.message_id
    while new_message_id > 1:
        try:
            bot.delete_message(chat_id=message.chat.id, message_id=new_message_id)
        except Exception as error:
            print(f'Message_id does not exist: {new_message_id} - {error}')
        new_message_id = new_message_id - 1

    start(msg)
    print('clear.end;')


@bot.callback_query_handler(func=lambda c: c.data == TEST.callback_data)
def test(msg):
    print('test.enter;')
    keyboard = get_list_kbrd_from(elements=get_all_title(), prefix='remove_title_')
    bot.send_message(chat_id=msg.message.chat.id, text='test text', reply_markup=keyboard)
    print('test.end;')


@bot.callback_query_handler(func=lambda c: c.data.startswith('remove_title_'))
def remove_title(msg):
    print('remove_title.enter;', msg.data)
    test(msg)
    #todo нельзя удалить если заголовок принадлежит заметке
    title_id = int(str(msg.data).removeprefix('remove_title_'))
    remove_title_by_id(title_id)

    print('remove_title.end;')


@bot.message_handler(content_types=['text'])
def handle_text(msg):
    print('handle_text.enter;')
    msg_text = msg.text
    keyboard = types.InlineKeyboardMarkup()
    add_title_key = types.InlineKeyboardButton(text='Add Title', callback_data='add_title')
    keyboard.add(add_title_key)
    bot.send_message(chat_id=msg.chat.id, text=msg_text, reply_markup=keyboard)
    print('handle_text.end;')


@bot.callback_query_handler(func=lambda c: c.data == 'add_title')
def handle_add_title_key(msg):
    print('handle_add_title_key.enter;')
    add_title_orm(title_name=msg.message.htm)
    print('handle_add_title_key.end;')


# @bot.callback_query_handler(func=lambda message: message.data == CLEAR_BTN.callback_data)
# def clear_kay(msg):
#     print('clear_kay.enter;')
#     new_message_id = message.message.message_id
#     # bot.delete_message(chat_id=message.message.chat.id, message_id=263)
#
#     while new_message_id > 1:
#         try:
#             bot.delete_message(chat_id=message.message.chat.id, message_id=new_message_id)
#         except Exception as error:
#             print(f'Message_id does not exist: {new_message_id} - {error}')
#         new_message_id = new_message_id - 1
#     print('clear_kay.end;')


bot.polling(none_stop=True)
