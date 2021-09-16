from graphene import (String, ObjectType, Field, Mutation, List, Int, ID)

from demoGql.resolvers import resolve_posts, resolve_followers
from demoGql.schema import UserPostOutType, UserOutType
from demoGql.services.users import UserService
from demoGql.utils import dev_log


class UserType(ObjectType):
    id = ID()
    username = String()
    email = String()
    posts = Field(List(UserPostOutType), resolver=resolve_posts)
    followers = Field(List(UserOutType), last=Int(required=True), resolver=resolve_followers)


class CreateUser(Mutation):
    class Arguments:
        username = String(required=True)
        email = String(required=True)
        password = String(required=True)

    user = Field(UserOutType)

    @dev_log
    def mutate(self, info, username: str, email: str, password: str):
        created_user = UserService().create_user(username, email, password)
        user = UserOutType(username=created_user.username, email=created_user.email, id=created_user.id)
        return CreateUser(user=user)
