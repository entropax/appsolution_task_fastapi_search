import datetime
from typing import List

from pydantic import BaseModel


class PostRemoveItem(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Post(PostRemoveItem):
    text: str
    rubrics: List[str]
    created_date: datetime.datetime

    class Config:
        orm_mode = True
