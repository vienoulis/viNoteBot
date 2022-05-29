from data.orm import *

init_note_db()

log_note()
add_note(title_name="TEST 3", text_note="I love my love")
remove_by_id(4)
# get_notes_by_id()
# print('')
# remove_by_title("test titile for delete")
# print('')
log_note()
