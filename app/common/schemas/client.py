from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ClientCreate(BaseModel):
    name: str
    address: str
    city: str
    country: str
    goverment_id: str = Field(..., alias="govermentId")
    contact_name: Optional[str] = Field(None, alias="contactName")
    contact_phone: Optional[str] = Field(None, alias="contactPhone")
    contact_email: Optional[str] = Field(None, alias="contactEmail")
    # TODO: Extract from token (Delete from here)
    user_id: UUID = Field(..., alias="userId")


class ClientResponse(ClientCreate):
    id: UUID
    is_active: bool = Field(..., alias="isActive")
    created_at: datetime = Field(..., alias="createdAt")
    modified_on: datetime = Field(..., alias="modifiedOn")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
