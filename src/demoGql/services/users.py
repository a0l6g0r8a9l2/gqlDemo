from fastapi import (
    HTTPException,
    status, )

from demoGql.database import Session
from demoGql import tables


class UserService:
    def __init__(self, session: Session = Session()):
        self.session = session

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

    def create_user(self, name: str, email: str, password: str) -> tables.User:
        user = tables.User(
            email=email,
            name=name,
            password=password
        )

        with self.session:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
        return user
