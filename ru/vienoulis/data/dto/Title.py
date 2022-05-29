import peewee
from ru.vienoulis.data.orm import db


class Title(peewee.Model):
    name = peewee.CharField(unique=True, null=False)

    class Meta:
        database = db
