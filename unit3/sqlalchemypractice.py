__author__ = 'apowers411'

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

engine = create_engine('sqlite:///:memory:', echo= True)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column (String)
    password = Column (String)
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.name, self.fullname, self.password)
Base.metadata.create_all(engine)

# instances
ed_user = User('ed','Ed Jones', 'edspassword')

#Sessions
from sqlalchemy.orm import sessionmaker
#create master session
Session = sessionmaker()
#connect to engine
Session.configure(bind=engine)
#then make little sessions
session = Session()
#you can add, query and then filter_by
#in order for something to persist you need to use session
session.add(ed_user)

ed_user.password = 'notnewpassword'

#session (does not work after query)
session.dirty
#to make the changes not pending but
session.commit()

#Query
for instance in session.query(User).order_by(User.id):
    print instance.name, instance.fullname

#Query(better)
for name, fullname in session.query(User.name, User.fullname):
    print name, fullname
#Query(tuples)
for row in session.query(User, User.name).all():
    print row.User, row.name

#Query limit and offset is done with slices [1:3]
for u in session.query(User).order_by(User.id)[1:3]:
    print u
#
# Quickie Intro to Object States
#
# It’s helpful to know the states which an instance can have within a session:
#
# Transient - an instance that’s not in a session, and is not saved to the database; i.e. it has no database identity. The only relationship such an object has to the ORM is that its class has a mapper() associated with it.
# Pending - when you add() a transient instance, it becomes pending. It still wasn’t actually flushed to the database yet, but it will be when the next flush occurs.
# Persistent - An instance which is present in the session and has a record in the database. You get persistent instances by either flushing so that the pending instances become persistent, or by querying the database for existing instances (or moving persistent instances from other sessions into your local session).
# Detached - an instance which has a record in the database, but is not in any session. There’s nothing wrong with this, and you can use objects normally when they’re detached, except they will not be able to issue any SQL in order to load collections or attributes which are not yet loaded, or were marked as “expired”.
# Knowing these states is important, since the Session tries to be strict about ambiguous operations (such as trying to save the same object to two different sessions at the same time).

#count is best adding .count to end of a query

#relationships
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref=backref('addresses',order_by=id))
    def __init__(self,email_address):
        self.email_address = email_address
    def __repr__(self):
        return "<Address('%s')>" % self.email_address

#joins
query.join(Address, User.id==Address.user_id)    # explicit condition
query.join(User.addresses)                       # specify relationship from left to right
query.join(Address, User.addresses)              # same, with explicit target
query.join('addresses')                          # same, using a string

#Cascading deletes require explicit attribute in the relationship
addresses = relationship("Address", backref='user', cascade="all, delete, delete-orphan")

#for a many-to-many relationship you have to create an assocation table
from sqlalchemy import Table, Text
post_keywords= Table('post_keywords', Base.metadata, Column('post_id',Integer,ForeignKey('posts.id')),
                     Column('keyword_id',Integer,ForeignKey('keywords.id'))
)

#!!!!don't understanding the loader strategy and when stuff gets created
#memory intensive (lazy-select, dynamic- returns a query object)
#how you are writing your query and need to speed up

##how far does a session rollback go

#module is a single time and package
__init__.py makes into module
that allows other things to run it

get run.py





