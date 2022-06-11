from telebot import *

from ru.vienoulis.data.dto.Note import Note
from ru.vienoulis.data.orm import get_all_title
from ru.vienoulis.service.keybords import get_started_kbrd, get_list_kbrd_from, get_note_keyboard
from ru.vienoulis.di.conf import bot


def remove_msg(message):
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
    except Exception as error:
        print(f'Message_id does not exist: {error}')


def start_cmd(msg):
    bot.send_message(chat_id=msg.chat.id, text='Hello app was started', reply_markup=get_started_kbrd())


def clear_btn(msg):
    print('clear_kay.enter;')
    new_message_id = msg.message.message_id
    while new_message_id > 1:
        try:
            bot.delete_message(chat_id=msg.message.chat.id, message_id=new_message_id)
        except Exception as error:
            print(f'Message_id does not exist: {new_message_id} - {error}')
        new_message_id = new_message_id - 1


def show_title_btn(msg):
    keyboard = get_list_kbrd_from(elements=get_all_title(), prefix='title_')
    bot.send_message(chat_id=msg.message.chat.id, text='Titles: ', reply_markup=keyboard)


def show_notes_by_title_id_btn(msg):
    title_id = int(str(msg.data).removeprefix('title_'))
    note = Note.get_or_none(title_id=title_id)
    bot.send_message(chat_id=msg.message.chat.id, text=note.text, reply_markup=get_note_keyboard(note.id))


def send_add_title_btn(msg):
    print('send_add_title_btn.enter;')
    msg_text = msg.text
    keyboard = types.InlineKeyboardMarkup()
    add_title_key = types.InlineKeyboardButton(text='Add Title', callback_data='add_title')
    keyboard.add(add_title_key)
    bot.send_message(chat_id=msg.chat.id, text=msg_text, reply_markup=keyboard)
    print('send_add_title_btn.end;')
