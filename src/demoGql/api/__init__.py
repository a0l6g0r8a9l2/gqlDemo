import graphene
from fastapi import APIRouter
from graphene import ObjectType, Field, ID
from starlette.graphql import GraphQLApp

from . import (
    users,
)
from .users import CreateUser, UserType
from .posts import CreatePost, GetPost
from ..resolvers import resolve_user


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()


class Query(ObjectType):
    user = Field(UserType, id=ID(required=True), resolver=resolve_user)


router = APIRouter()
router.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))
