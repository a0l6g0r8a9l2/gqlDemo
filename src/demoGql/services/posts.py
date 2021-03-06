from typing import Optional, List
import logging

from fastapi import (
    HTTPException,
    status, )

from demoGql.database import Session
from demoGql import tables
from demoGql.schema import UserOutType
from demoGql.utils import dev_log

logging.basicConfig(level=logging.INFO)


class PostsService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def get_post_by_id(self, post_id: int) -> Optional[tables.Post]:
        with self.session:
            post = (
                self.session
                    .query(tables.Post)
                    .filter(tables.Post.id == post_id)
                    .first()
            )

        if not post:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return post

    @dev_log
    def get_posts_by_user_id(self, user_id: int) -> List[tables.Post]:
        with self.session:
            posts = (
                self.session
                    .query(tables.Post)
                    .filter(tables.Post.posted_by == user_id)
                    .all()
            )
        return posts

    def create(self, title: str, content: str, posted_by: UserOutType) -> tables.Post:
        post = tables.Post(
            title=title,
            content=content,
            posted_by=posted_by.id
        )

        with self.session:
            self.session.add(post)
            self.session.commit()
            self.session.refresh(post)
        return post
