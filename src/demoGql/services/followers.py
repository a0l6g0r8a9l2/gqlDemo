from typing import List

from fastapi import (
    HTTPException,
    status, )

from demoGql.database import Session
from demoGql import tables


class FollowersService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def follow_up(self, user_id: int, follow_up_user_id: int):
        follower = tables.Follower(
            id=user_id
        )
        user_to_follow = (
            self.session
                .query(tables.User)
                .filter(tables.User.id == follow_up_user_id)
                .first()
        )

        user_to_follow.follower.append(follower)

        if not user_to_follow:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        with self.session:
            self.session.add(user_to_follow)
            self.session.commit()
            self.session.refresh(user_to_follow)
        return user_to_follow

    def get_user_followers(self, user_id: int) -> List[tables.User]:
        with self.session:
            _followers = (
                self.session
                    .query(tables.User)
                    .filter(tables.User.id == user_id)
                    .first()
                    .follower
            )

            followers_id = [item.id for item in _followers]

            followers = (
                self.session
                    .query(tables.User)
                    .filter(tables.User.id.in_(followers_id))
                    .all()
            )
        return followers
