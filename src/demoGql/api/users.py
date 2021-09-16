from graphene import (String, ObjectType, Field, Mutation, List, Int, ID)

from demoGql.resolvers import resolve_posts, resolve_followers
from demoGql.schema import UserPostOutType, UserOutType
from demoGql.services.users import UserService
from demoGql.utils import dev_log


class UserType(ObjectType):
    """
    Автор/юзер. Его посты и подписчики
    """
    id = ID(description="Ид пользователя/автора")
    username = String(description="Имя пользователя/автора")
    email = String(description="email пользователя/автора")
    posts = Field(List(UserPostOutType), resolver=resolve_posts, description="Посты пользователя/автора")
    followers = Field(List(UserOutType),
                      last=Int(required=True, description="Сколько подписчиков вернуть"),
                      resolver=resolve_followers,
                      description="Подписчики пользователя/автора")


class CreateUser(Mutation):
    """
    Создать нового юзера
    """
    class Arguments:
        username = String(required=True, description="Имя пользователя")
        email = String(required=True, description="email пользователя")
        password = String(required=True, description="Пароль пользователя")

    user = Field(UserOutType)

    @dev_log
    def mutate(self, info, username: str, email: str, password: str):
        created_user = UserService().create_user(username, email, password)
        user = UserOutType(username=created_user.username, email=created_user.email, id=created_user.id)
        return CreateUser(user=user)
