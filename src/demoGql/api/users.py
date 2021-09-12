from graphene import (String, ObjectType, Field, Mutation, List)

from demoGql.models import UserCreate
from demoGql.resolvers import resolve_posts
from demoGql.schema import User, UserPostOutType, UserOutType
from demoGql.services.users import UserService
from demoGql.utils import dev_log


class UserType(ObjectType):
    posts = Field(List(UserPostOutType), resolver=resolve_posts)
    user = Field(UserOutType)

    def resolve_user(self: UserOutType, info):
        return UserOutType(username=self.username, email=self.email, id=self.id)


class CreateUser(Mutation):
    class Arguments:
        username = String()
        email = String()
        password = String()

    user = Field(User)

    @dev_log
    def mutate(root, info, username, email, password):
        model = UserCreate(username=username, email=email, password=password)
        created_user = UserService().create_user(model)
        user = User(username=created_user.username, email=created_user.email, id=created_user.id)
        return CreateUser(user=user)
