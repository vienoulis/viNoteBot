from telebot import types

from ru.vienoulis.utils.button import *

TEST = Button('Test button', 'test')
SHOW_TITLES_LIST_BTN = Button('Show Titles', 'showBtn')
CLEAR_BTN = Button('Clear', 'clearBtn')
REMOVE_BTN = Button('Remove', 'remove_title')
HOME_BTN = Button('Home', 'homeBtn')
ADD_TITLE_BTN = Button('Add title', 'add_title')
ADD_NOTE_BTN = Button('Add note', 'add_note')


class InlineBtn(object):
    ADD_TITLE_BTN = types.InlineKeyboardButton(text=ADD_TITLE_BTN.text, callback_data=ADD_TITLE_BTN.callback_data)
    ADD_NOTE_BTN = types.InlineKeyboardButton(text=ADD_NOTE_BTN.text, callback_data=ADD_NOTE_BTN.callback_data)
    HOME_BTN = types.InlineKeyboardButton(text=HOME_BTN.text, callback_data=HOME_BTN.callback_data)


