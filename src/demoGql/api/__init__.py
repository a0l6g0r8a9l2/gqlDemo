import graphene
from fastapi import APIRouter
from graphene import ObjectType, Field, ID
from starlette.graphql import GraphQLApp

from demoGql.api.followers import FollowUp
from demoGql.api.posts import CreatePost, GetPost
from demoGql.api.users import CreateUser, UserType
from demoGql.resolvers import resolve_user


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
    follow_up = FollowUp.Field()


class Query(ObjectType):
    """
    Автор/юзер.
    """
    user = Field(UserType, id=ID(required=True, description="Ид пользователя"), resolver=resolve_user)


schema = graphene.Schema(query=Query, mutation=Mutation)
router = APIRouter()
router.add_route("/", GraphQLApp(schema=schema))
