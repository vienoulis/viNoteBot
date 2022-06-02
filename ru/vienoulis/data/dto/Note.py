from ru.vienoulis.data.dto.Title import *


class Note(peewee.Model):
    title = peewee.ForeignKeyField(Title)
    text = peewee.TextField()

    class Meta:
        database = db
