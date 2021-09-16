from graphene import (String, ObjectType, ID, DateTime, List, Field)


class UserPostOutType(ObjectType):
    """
    Пост
    """
    post_id = ID(description="Ид поста")
    title = String(description="Заголовок поста")
    content = String(description="Контент поста")
    date = DateTime(description="Дата создания поста")


class UserOutType(ObjectType):
    """
    Юзер. Может быть автором постов или фоловером
    """
    username = String(description="Имя пользователя")
    email = String(description="email пользователя")
    id = ID(description="Ид пользователя")


class User(UserOutType):
    """
    Юзер с постами и фоловером
    """
    posts = List(UserPostOutType, description="Список постов пользователя")
    followers = List(UserOutType, description="Список подписчиков пользователя")


class PostOutType(UserPostOutType):
    """
    Пост и его автор
    """
    author = Field(UserOutType)
