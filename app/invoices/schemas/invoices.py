from uuid import UUID

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class InvoiceBase(BaseModel):
    invoice_num: int
    user_id: UUID
    client_id: UUID
    detail: str
    total: float


class InvoiceResponse(InvoiceBase):
    id: UUID
    created_at: datetime
    modified_on: datetime

    class Config:
        orm_mode = True
