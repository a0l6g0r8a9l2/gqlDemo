from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    func, Table
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table('users_followers', Base.metadata,
                          Column('user_id', ForeignKey('users.id'), primary_key=True),
                          Column('follower_id', ForeignKey('followers.id'), primary_key=True)
                          )


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String, unique=True)
    password = Column(String)

    follower = relationship("Follower",
                            secondary=association_table,
                            backref="parents")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    posted_by = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime(timezone=True), server_default=func.now())
    title = Column(String)
    content = Column(String)

    user = relationship('User', backref='posts')


class Follower(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True)
    follow_from_date = Column(DateTime(timezone=True), server_default=func.now())
