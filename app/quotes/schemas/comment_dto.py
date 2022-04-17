from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class CommentBase(BaseModel):
    comment: str
    created_at: datetime
    modified_on: datetime


class CommentCreate(CommentBase):
    quote_id: UUID


class CommentResponse(CommentBase):
    id: UUID

    class Config:
        orm_mode = True
