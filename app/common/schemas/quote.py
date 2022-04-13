from uuid import UUID
from psycopg2 import Date
from pydantic import BaseModel
from datetime import datetime

from sqlalchemy import null


class QuoteBase(BaseModel):
    quote_num: int
    user_id: UUID
    # date: datetime


class QuoteCreate(QuoteBase):
    pass


class QuoteResponse(BaseModel):
    id: UUID
    quote_num: int
    user_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True


class HttpResponse(BaseModel):
    status_code: str
    message: str
