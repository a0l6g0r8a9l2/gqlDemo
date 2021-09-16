from graphene import (String, ObjectType, ID, DateTime, List, Field)


class UserPostOutType(ObjectType):
    post_id = ID()
    title = String()
    content = String()
    date = DateTime()


class UserOutType(ObjectType):
    username = String()
    email = String()
    id = ID()


class User(UserOutType):
    posts = List(UserPostOutType)
    followers = List(UserOutType)


class PostOutType(UserPostOutType):
    author = Field(UserOutType)
