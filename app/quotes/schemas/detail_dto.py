from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class DetailBase(BaseModel):
    valid_time: datetime
    deliver_time: datetime
    currency_type: str
    sub_total: float
    total_expense: float


class DetailCreate(DetailBase):
    pass


class DetailResponse(DetailBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
