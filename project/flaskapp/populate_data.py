import twitter
import wikipedia
import dstk
from app.models import Person
from flask.ext.mongoengine import MongoEngine

#How do I reference something one level higher

names=["oprah winfrey","nelson mandela","nina simone","albert einstein","beyonce","jill scott","barack obama"]
output=[]
for n in names:
    n=Person(name=n,bio=wikipedia.summary(n)).save()
