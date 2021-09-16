from graphene import (String, ObjectType, Field, ID, Mutation)

from demoGql.resolvers import resolve_user, resolve_post
from demoGql.schema import UserPostOutType, PostOutType
from demoGql.services.posts import PostsService
from demoGql.utils import dev_log


class GetPost(ObjectType):
    post = Field(UserPostOutType, resolver=resolve_post, post_id=ID(required=True))


class CreatePost(Mutation):
    """
    Создать пост
    """
    class Arguments:
        title = String(required=True, description="Заголовок поста")
        content = String(required=True, description="Контент поста")
        posted_by = ID(required=True, description="Ид автора")

    post = Field(PostOutType)

    @dev_log
    def mutate(self, info, title: str, content: str, posted_by: int):
        user = resolve_user(self, info=info, id=posted_by)

        created_post = PostsService().create(title=title, content=content, posted_by=user)
        post = PostOutType(
            title=created_post.title,
            content=created_post.content,
            post_id=created_post.id,
            date=created_post.date,
            author=user
        )
        return CreatePost(post=post)
