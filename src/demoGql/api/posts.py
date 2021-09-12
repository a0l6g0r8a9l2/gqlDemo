from graphene import (String, ObjectType, Field, ID, Mutation, List)

from demoGql.resolvers import resolve_user, resolve_post
from demoGql.models import PostCreate
from demoGql.schema import UserPostOutType, UserPostOutType
from demoGql.services.posts import PostsService
from demoGql.utils import dev_log


class GetPost(ObjectType):
    post = Field(UserPostOutType, resolver=resolve_post, post_id=ID(required=True))
    # posts_by_user = Field(List(BasePost), resolver=resolve_user_posts, user_id=ID(required=True))


# class GetPosts(ObjectType):
#     posts = List(Post)
#
#     @dev_log
#     def resolve_posts(self, info, user_id: int):
#         # user = resolve_user(self, info=info, id=post_id)
#
#         get_post = PostsService().get_posts_by_user_id(user_id=user_id)
#         return Post(
#             title=get_post.title,
#             content=get_post.content,
#             id=get_post.id,
#             date=get_post.date,
#             posted_by=user
#         )


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
