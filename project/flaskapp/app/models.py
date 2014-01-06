import datetime
from flask import url_for
from app import db


class Person(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now,required=True)
    name = db.StringField(max_length=6000, required=True)
    bio = db.StringField(max_length=6000, required=True)
    tags = db.ListField(db.EmbeddedDocumentField('Tag'))

    def get_absolute_url(self):
        return url_for('person',kwargs={"name":self.name})

    def __unicode__(self):
        return self.bio

    meta = {
        'allow_inheritance':True,
        'indexes':['-created_at','name'],
        'ordering':['-created_at']
    }

class Tag(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    positive = db.StringField(verbose_name="Positive Comment", required=True)
    negative = db.StringField(verbose_name="Negative Comment", required=False)
