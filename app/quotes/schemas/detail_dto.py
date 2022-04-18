from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class DetailBase(BaseModel):
    valid_time: int
    deliver_time: datetime
    currency_type: str
    payment_terms: str
    created_at: datetime
    modified_on: datetime
    sub_total: float
    total: float


class DetailCreate(DetailBase):
    quote_id: UUID


class DetailResponse(DetailBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
