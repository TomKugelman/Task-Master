from flask_login import UserMixin
from flask_sqlalchemy import sqlalchemy
from sqlalchemy import (
    create_engine, 
    Column, 
    Integer, 
    String, 
    ForeignKey,
    DateTime,
    Float,
)
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import json
from json import JSONEncoder as BaseEncoder

# Setup SQLAlchemy engine 
engine = create_engine('sqlite:///TaskMaster.db', connect_args={'check_same_thread': False}, echo=True)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()
Base.metadata.create_all(engine)

def Add_Entry(entry):
    session.add(entry)
    session.commit()

def Delete(entry):
    session.delete(entry)
    session.commit()

def Check(user_id):
    result = session.query(User).get(user_id)
    #print("------------------------------------------------")
    #print("result: ", result.id, " \ ", user_id)
    if result == None:
        return False
    else:
        return True

class User(UserMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def asdict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}
    
    @staticmethod
    def get(user_id):
        result = session.query(User).get(user_id)
        user = User(result.id, result.name, result.email)
        return user
    
    def is_authenticated():
        return True
    
    def is_active():
        return True
    
    def is_anonymous():
        return False
        
class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='tasks')

    def __init__(self, content, user):
        self.content = content
        self.user_id = user

class JSONEncoder(BaseEncoder):
    def default(self, object):
        return object.asdict()
