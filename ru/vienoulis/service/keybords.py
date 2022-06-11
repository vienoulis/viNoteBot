from telebot import types

from ru.vienoulis.utils.const.buttoms import *


def get_started_kbrd():
    keyboard = types.InlineKeyboardMarkup()
    test_btn = types.InlineKeyboardButton(text=TEST.text, callback_data=TEST.callback_data)
    show_titles_btn = types.InlineKeyboardButton(text=SHOW_TITLES_LIST_BTN.text, callback_data=SHOW_TITLES_LIST_BTN.callback_data)
    clear_btn = types.InlineKeyboardButton(text=CLEAR_BTN.text, callback_data=CLEAR_BTN.callback_data)
    keyboard.add(show_titles_btn, clear_btn, test_btn)
    return keyboard


def get_list_kbrd_from(elements, prefix):
    keyboard = types.InlineKeyboardMarkup()
    for el in elements:
        keyboard.add(types.InlineKeyboardButton(text=el.name, callback_data=prefix + str(el.id)))
    return keyboard


def get_note_keyboard(note_id):
    keyboard = types.InlineKeyboardMarkup()
    remove_key = types.InlineKeyboardButton(text=REMOVE_BTN.text, callback_data=f'{REMOVE_BTN.callback_data}_{note_id}')
    start_key = types.InlineKeyboardButton(text=HOME_BTN.text, callback_data=HOME_BTN.callback_data)
    keyboard.add(remove_key, start_key)
    return keyboard
