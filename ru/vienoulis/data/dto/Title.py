import peewee

from ru.vienoulis.di.conf import db


class Title(peewee.Model):
    id = peewee.PrimaryKeyField
    name = peewee.CharField(unique=True, null=False)

    class Meta:
        database = db
