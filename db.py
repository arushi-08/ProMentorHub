import datetime

from mongoengine import connect
from flask_mongoengine import MongoEngine

db = MongoEngine()

connect(
    host="mongodb://127.0.0.1:27017/mentor_app?authSource=admin",
    alias="db",
)


class User(db.Document):
    # id = db.IntField()
    public_id = db.StringField()
    name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    age = db.IntField()
    city = db.StringField()
    state = db.StringField()
    country = db.StringField()
    meta = {"db_alias": "db"}


class Diary(db.Document):
    name = db.StringField()
    date = db.DateTimeField(default=datetime.datetime.utcnow)
    mood = db.StringField()
    sleep = db.IntField()
    note = db.StringField()
    meta = {"db_alias": "db"}


class Weather(db.Document):
    city = db.StringField()
    date = db.DateTimeField(default=datetime.datetime.utcnow)
    temperature = db.StringField()
    pressure = db.StringField()
    humidity = db.StringField()
    weather = db.StringField()
    meta = {"db_alias": "db"}

class Mentor(db.Document):
    first_name = db.StringField()
    last_name = db.StringField()
    job_title = db.StringField()
    company_name = db.StringField()
    company_desc = db.StringField()
    job_desc = db.StringField()
    job_requirement = db.StringField()
    salary = db.StringField()
    location = db.StringField()
    employment_type = db.StringField()
    department = db.StringField()
    label = db.StringField()
    meta = {"db_alias": "db"}
