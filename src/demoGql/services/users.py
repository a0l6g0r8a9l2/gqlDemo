from fastapi import (
    HTTPException,
    status, )

from demoGql.database import Session
from .. import (
    models,
    tables,
)


class UserService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def get_user_by_name(self, username: str) -> tables.User:
        with self.session:
            user = (
                    self.session
                    .query(tables.User)
                    .filter(tables.User.username == username)
                    .first()
            )

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return user

    def get_user_by_id(self, id: int) -> tables.User:
        with self.session:
            user = (
                    self.session
                    .query(tables.User)
                    .filter(tables.User.id == id)
                    .first()
            )

        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return user

    def create_user(self, user_data: models.UserCreate) -> tables.User:
        user = tables.User(
            email=user_data.email,
            username=user_data.username,
            password=user_data.password
        )

        with self.session:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
        return user
