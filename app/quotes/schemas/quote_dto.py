from uuid import UUID

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from app.quotes.schemas.comment_dto import CommentBase, CommentResponse

from app.quotes.schemas.detail_dto import DetailBase, DetailResponse
from app.quotes.schemas.item_dto import ItemBase, ItemResponse
from app.quotes.schemas.tax_dto import TaxBase, TaxResponse


class QuoteBase(BaseModel):
    quote_num: int
    exp_date: datetime
    quote_status: Optional[bool]
    # TODO: extract from token
    user_id: UUID
    client_id: UUID


class QuoteCreate(BaseModel):
    quote: QuoteBase
    detail: Optional[DetailBase]
    item: Optional[List[ItemBase]]
    taxes: Optional[List[TaxBase]]
    comment: Optional[CommentBase]


class QuoteResponse(BaseModel):
    id: UUID
    quote_num: int
    user_id: UUID
    created_at: datetime
    client_id: UUID
    exp_date: datetime
    quote_status: bool

    class Config:
        orm_mode = True


class HttpResponse(BaseModel):
    status_code: str
    message: str


class QuoteResponses(QuoteResponse):
    details: Optional[List[DetailResponse]]
    items: Optional[List[ItemResponse]]
    taxes: Optional[List[TaxResponse]]
    comments: Optional[List[CommentResponse]]

    class Config:
        orm_mode = True


class QuoteUpdate(BaseModel):
    id: UUID
    quote_num: Optional[int]
    # TODO: extract from token
    user_id: UUID
    client_id: UUID
    exp_date: Optional[datetime]
    quote_status: Optional[bool]
