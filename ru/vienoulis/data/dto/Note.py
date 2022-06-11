from ru.vienoulis.data.dto.Title import *
from ru.vienoulis.di.conf import db


class Note(peewee.Model):
    id = peewee.PrimaryKeyField
    title = peewee.ForeignKeyField(Title)
    text = peewee.TextField()

    class Meta:
        database = db
