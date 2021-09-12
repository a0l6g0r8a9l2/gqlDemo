from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    func
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password = Column(String)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    posted_by = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime(timezone=True), server_default=func.now())
    title = Column(String)
    content = Column(String)

    user = relationship('User', backref='posts')
