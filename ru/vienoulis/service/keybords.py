from telebot import types


def get_started_kbrd():
    keyboard = types.InlineKeyboardMarkup()
    test_btn = types.InlineKeyboardButton(text=TEST.text, call=TEST.callback_data)
    show_titles_btn = types.InlineKeyboardButton(text=SHOW_TITLE_BTN.text, callback_data=SHOW_TITLE_BTN.callback_data)
    clear_btn = types.InlineKeyboardButton(text=CLEAR_BTN.text, callback_data=CLEAR_BTN.callback_data)
    keyboard.add(show_titles_btn, clear_btn, test_btn)
    return keyboard


def get_list_kbrd_from(elements, prefix):
    keyboard = types.InlineKeyboardMarkup()
    for el in elements:
        keyboard.add(types.InlineKeyboardButton(text=el.name, callback_data=prefix + str(el.id)))
    return keyboard
