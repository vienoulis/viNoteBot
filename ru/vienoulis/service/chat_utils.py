from telebot import *

from ru.vienoulis.data.dto.Note import Note
from ru.vienoulis.data.orm import get_all_title
from ru.vienoulis.di.conf import bot
from ru.vienoulis.service.keybords import get_started_kbrd, get_list_kbrd_from, get_note_list_keyboard, \
    get_empty_note_list_keyboard
from ru.vienoulis.utils.const.buttoms import ADD_TITLE_BTN, ADD_NOTE_BTN, InlineBtn


def remove_msg(message, increment=0):
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.id - increment)
    except Exception as error:
        print(f'Message_id does not exist: {error}')


def start_cmd(chat):
    bot.send_message(chat_id=chat.id, text='Hello app was started', reply_markup=get_started_kbrd())


def clear_btn(msg):
    print('clear_kay.enter;')
    new_message_id = msg.message.message_id
    while new_message_id > 1:
        try:
            bot.delete_message(chat_id=msg.message.chat.id, message_id=new_message_id)
        except Exception as error:
            print(f'Message_id does not exist: {new_message_id} - {error}')
            break
        new_message_id = new_message_id - 1


def show_title_btn(msg):
    keyboard = get_list_kbrd_from(elements=get_all_title(), prefix='title_')
    bot.send_message(chat_id=msg.message.chat.id, text='Titles: ', reply_markup=keyboard)


def show_notes_by_title_id_btn(msg):
    title_id = int(str(msg.data).removeprefix('title_'))
    if Note.get_or_none(title=title_id) is None:
        bot.send_message(chat_id=msg.message.chat.id, text='This title is empty',
                         reply_markup=get_empty_note_list_keyboard(title_id))
    else:
        notes = Note.select().where(Note.title == title_id)
        bot.send_message(chat_id=msg.message.chat.id, text='Menu',
                         reply_markup=get_note_list_keyboard())
        for note in notes:
            bot.send_message(chat_id=msg.message.chat.id, text=f'{note.text}')


def send_add_note_title_btn(msg):
    print('send_add_note_title_btn.enter;')
    msg_text = msg.text
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(InlineBtn.ADD_TITLE_BTN, InlineBtn.ADD_NOTE_BTN, InlineBtn.HOME_BTN)
    bot.send_message(chat_id=msg.chat.id, text=msg_text, reply_markup=keyboard)
    print('send_add_note_title_btn.end;')


def send_add_note_btn(msg):
    print('send_add_note_btn.enter;')
    msg_text = msg.text
    keyboard = types.InlineKeyboardMarkup()
    add_note_key = types.InlineKeyboardButton(text='Add Note', callback_data='add_note')
    keyboard.add(add_note_key)
    bot.send_message(chat_id=msg.chat.id, text=msg_text, reply_markup=keyboard)
    print('send_add_note_btn.end;')
