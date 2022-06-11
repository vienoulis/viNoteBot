from ru.vienoulis.data.dto.Note import *
from ru.vienoulis.data.dto.Title import *


def init_note_db():
    print("init_note_db.enter;")
    Title.create_table()
    Note.create_table()
    print("init_note_db.success;")


def add_note(title_name, text_note):
    print("add_note.enter; title", title_name, "text", text_note)
    title, created = Title.get_or_create(name=title_name)
    note = Note(title=title.id, text=text_note)
    note.save()
    print("add_note.success;")


def add_title_orm(title_name):
    print("add_title.enter; title", title_name)
    title, created = Title.get_or_create(name=title_name)
    if created:
        title.save()
        print("add_title.saved;")
    print("add_title.success;")


def log_note():
    print("get_notes.enter;")

    print('--- Note ---')
    for note in Note.filter():
        title_name = Title.get_by_id(note.title).name

        print('||', note.id, '|', title_name, '|', note.text, '||')
    print("get_notes.success;")


def log_title():
    print("get_notes.enter;")
    print('--- Note ---')
    for title in Title.filter():
        print('||', title.id, '|', title.name, '||')
    print("get_notes.success;")


def remove_by_id(note_id):
    print("remove_by_id.enter; id", note_id)
    note = Note.get_or_none(Note.id == note_id)

    if note is not None:
        print("remove_by_id.not_none; note", note)
        note.delete_instance()
    else:
        print("note id", note_id, "non existent")

    print("remove_by_id.success;")


def remove_title_by_id(title_id):
    print("remove_title_by_id.enter; id", title_id)
    title = Title.get_or_none(Title.id == title_id)

    if title is not None:
        print("remove_title_by_id.not_none; title", title)
        title.delete_instance()
    else:
        print("title id", title_id, "non existent")

    print("remove_title_by_id.success;")


def get_title_by_id(title_id):
    print("get_title_by_id.enter; id", title_id)
    title = Title.get_or_none(Title.id == title_id)
    print(f"get_title_by_id.success; {title}")
    return title


def get_all_title():
    return Title.filter()
# def remove_by_title(note_title):
#     print("remove_by_title.enter; title", note_title)
#     title = Title.get(Title.name == note_title)
#     note = Note.get_or_none(Note.title == title.id)
#
#     if note is not None:
#         print("remove_by_title.not_none; note", note)
#         note.delete_instance()
#     else:
#         print("note title", note_id, "non existent")
    #
    # print("remove_by_title.success;")
