from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

class ClientCreate(BaseModel):
    name: str
    address: str
    city: str
    country: str
    goverment_id: str
    # TODO: Extract from token (Delete from here)
    user_id: UUID


class ClientResponse(BaseModel):
    id: UUID
    name: str
    address: str
    city: str
    country: str
    is_active: bool
    goverment_id: str
    user_id: UUID
    created_at: datetime
    modified_on: datetime

    class Config:
        orm_mode = True
