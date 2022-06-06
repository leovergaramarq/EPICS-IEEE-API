import mongoengine as me

class Game(me.Document):
    code = me.StringField(required=True)
    name = me.StringField(required=True)
    level = me.StringField(required=True)
    topic = me.StringField()
    short_description = me.StringField(required=True)
    description = me.StringField()
    developers = me.ListField(me.DictField())
    launchDate = me.DateField()
    logo = me.URLField()
    id_school = me.StringField(required=True)

    meta = {'collection': 'games'}