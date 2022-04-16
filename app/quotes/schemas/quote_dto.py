from uuid import UUID

from typing import List
from datetime import datetime
from pydantic import BaseModel
from app.quote.schemas.comment_dto import CommentCreate

from app.quote.schemas.detail_dto import DetailCreate
from app.quote.schemas.item_dto import ItemCreate
from app.quote.schemas.tax_dto import TaxCreate


class QuoteBase(BaseModel):
    quote_num: int
    exp_date: datetime
    quote_status: bool
    user_id: UUID
    customer_id: UUID


class QuoteCreate(BaseModel):
    quote: QuoteBase
    detail: DetailCreate
    items: List[ItemCreate]
    taxes: List[TaxCreate]
    comment: CommentCreate


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
