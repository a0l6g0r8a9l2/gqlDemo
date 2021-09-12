from graphene import (String, ObjectType, ID, DateTime, List)


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


class PostOutType(UserPostOutType):
    posted_by_user_id = ID()