import mongoengine as me
from random import random, randrange

class Student(me.Document):
    class Representative(me.EmbeddedDocument):
        firstname = me.StringField()
        lastname = me.StringField()
        identity_doc = me.StringField()
        phone = me.DictField()
        
    username = me.StringField(required=True, unique=True)
    firstname = me.StringField(required=True)
    lastname = me.StringField(required=True)
    id_school = me.IntField(required=True)
    course = me.StringField()
    identity_doc = me.StringField(required=True, unique=True)
    doc_type = me.StringField(required=True)
    birth_date = me.DateTimeField(required=True)
    gender = me.StringField()
    photo = me.URLField(default='https://randomuser.me/api/portraits/{}men/{}.jpg'.format(
        'wo' if random() < 0.5 else '',
        randrange(0, 100)
    ))
    age = me.IntField()
    address = me.StringField()
    phone = me.DictField()
    email = me.StringField()
    legal_rep = me.EmbeddedDocumentField(Representative)
    meta = {'collection': 'students'}
