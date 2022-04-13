from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    first_name: str
    second_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str
    country: str
    city: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    class Config:
        orm_mode = True

class HttpResponse(BaseModel):
    status_code: str
    message: str