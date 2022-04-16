from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class CommentBase(BaseModel):
    comment: str


class CommentCreate(CommentBase):
    pass


class CommentResponse(CommentBase):
    comment: str
    created_at: datetime

    class Config:
        orm_mode = True
