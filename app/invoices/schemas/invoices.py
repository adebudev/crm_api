from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class InvoiceBase(BaseModel):
    invoice_num: int = Field(..., alias="invoiceNumber")
    user_id: UUID = Field(..., alias="userId")
    client_id: UUID = Field(..., alias="clientId")
    detail: str
    total: float


class InvoiceResponse(InvoiceBase):
    id: UUID
    created_at: datetime = Field(..., alias="createdAt")
    modified_on: datetime = Field(..., alias="modifiedOn")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
