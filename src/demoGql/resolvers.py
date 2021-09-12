from demoGql.schema import UserPostOutType, UserOutType, PostOutType
from demoGql.services.posts import PostsService
from demoGql.services.users import UserService
from demoGql.utils import dev_log


@dev_log
def resolve_user(parent, info, id: int):
    get_user = UserService().get_user_by_id(id=id)
    return UserOutType(username=get_user.username, email=get_user.email, id=get_user.id)


@dev_log
def resolve_posts(parent, info):
    _user_posts = PostsService().get_posts_by_user_id(parent.id)
    user_posts = [UserPostOutType(
        title=post.title,
        content=post.content,
        post_id=post.id,
        date=post.date,
    ) for post in _user_posts]
    return user_posts


@dev_log
def resolve_post(parent, info, post_id: int):
    post = PostsService().get_post_by_id(post_id=post_id)
    return PostOutType(
        title=post.title,
        content=post.content,
        post_id=post.id,
        date=post.date,
        posted_by_user_id=post.posted_by
    )
