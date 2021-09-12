from datetime import datetime

from pydantic import BaseModel

from demoGql.models import User


class BasePost(BaseModel):
    title: str
    content: str
    posted_by: User


class PostCreate(BasePost):
    pass


class PostUpdate(BasePost):
    pass


class Post(BasePost):
    id: int
    date: datetime

    class Config:
        orm_mode = True
