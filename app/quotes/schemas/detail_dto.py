from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class DetailBase(BaseModel):
    valid_time: int
    deliver_time: datetime
    currency_type: Optional[str]
    payment_terms: str
    sub_total: float
    total: float



class DetailResponse(DetailBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
