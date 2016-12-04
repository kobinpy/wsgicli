from peewee import *
from datetime import datetime

db = SqliteDatabase('sqlite:///')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.now)
    is_published = BooleanField(default=True)
