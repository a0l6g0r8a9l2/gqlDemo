from graphene import (String, ObjectType, Field, ID, Mutation)

from demoGql.models import PostCreate
from demoGql.resolvers import resolve_user, resolve_post
from demoGql.schema import UserPostOutType
from demoGql.services.posts import PostsService
from demoGql.utils import dev_log


class GetPost(ObjectType):
    post = Field(UserPostOutType, resolver=resolve_post, post_id=ID(required=True))


class CreatePost(Mutation):
    class Arguments:
        title = String(required=True)
        content = String(required=True)
        posted_by = ID(required=True)

    post = Field(UserPostOutType)

    @dev_log
    def mutate(self, info, title, content, posted_by):
        user = resolve_user(self, info=info, id=posted_by)

        model = PostCreate(title=title, content=content, posted_by=user)
        created_post = PostsService().create(model)
        post = UserPostOutType(
            title=created_post.title,
            content=created_post.content,
            id=created_post.id,
            date=created_post.date,
            posted_by=user
        )
        return CreatePost(post=post)
