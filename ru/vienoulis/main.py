from data.orm import add_title_orm, get_all_title, remove_title_by_id
from ru.vienoulis.di.conf import bot
from ru.vienoulis.service.chat_utils import remove_msg
from ru.vienoulis.service.chat_utils import start_cmd, clear_btn, show_title_btn, show_notes_by_title_id_btn, \
    send_add_title_btn
from ru.vienoulis.service.keybords import get_list_kbrd_from
from utils.const.buttoms import *


@bot.message_handler(commands=['start'])
def start_cmd_handler(msg):
    print('start_cmd_handler.enter;')
    start_cmd(msg)
    remove_msg(message=msg)
    print('start_cmd_handler.end;')


@bot.callback_query_handler(func=lambda message: message.data == CLEAR_BTN.callback_data)
def clear_btn_handler(msg):
    print('clear_btn_handler.enter;')
    clear_btn(msg)
    remove_msg(message=msg)
    start_cmd(msg.message)
    print('clear_btn_handler.end;')


@bot.callback_query_handler(func=lambda message: message.data == SHOW_TITLES_LIST_BTN.callback_data)
def show_titles_btn_handler(msg):
    print('show_titles_btn_handler.enter;')
    show_title_btn(msg)
    remove_msg(message=msg.message)
    print('show_titles_btn_handler.end;')


@bot.callback_query_handler(func=lambda c: c.data.startswith('title_'))
def show_title_by_id_handler(msg):
    print('show_title_by_id_handler.enter;', msg.data)
    show_notes_by_title_id_btn(msg)
    remove_msg(message=msg.message)
    print('show_title_by_id_handler.end;')


@bot.message_handler(content_types=['text'])
def text_handler(msg):
    print('text_handler.enter;')
    send_add_title_btn(msg)
    remove_msg(message=msg)
    remove_msg(message=msg, increment=1)
    print('text_handler.end;')


@bot.callback_query_handler(func=lambda c: c.data == HOME_BTN.callback_data)
def home_btn_handler(msg):
    print('home_btn_handler.enter;')
    start_cmd(msg.message)
    remove_msg(msg.message)
    print('home_btn_handler.end;')


@bot.callback_query_handler(func=lambda c: c.data == TEST.callback_data)
def test(msg):
    print('test.enter;')
    keyboard = get_list_kbrd_from(elements=get_all_title(), prefix='remove_title_')
    bot.send_message(chat_id=msg.message.chat.id, text='test text', reply_markup=keyboard)
    print('test.end;')


@bot.callback_query_handler(func=lambda c: c.data.startswith(f'{REMOVE_BTN.callback_data}_'))
def remove_title(msg):
    print('remove_title.enter;', msg.data)
    test(msg)
    # todo нельзя удалить если заголовок принадлежит заметке
    title_id = int(str(msg.data).removeprefix('remove_title_'))
    remove_title_by_id(title_id)

    print('remove_title.end;')


@bot.callback_query_handler(func=lambda c: c.data == 'add_title')
def handle_add_title_key(msg):
    print('handle_add_title_key.enter;')
    add_title_orm(title_name=msg.message.text)
    remove_msg(msg.message)
    start_cmd(msg)
    print('handle_add_title_key.end;')


bot.polling(none_stop=True)
