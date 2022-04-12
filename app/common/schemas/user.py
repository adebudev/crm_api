from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    first_name: str
    second_name: str
    last_name: str
    email: EmailStr
    password: str
    phone: str
    address: str
    country: str
    city: str

class UserUpdate(BaseModel):
    first_name: str
    second_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str
    country: str
    city: str

class UserResponse(BaseModel):
    id: UUID
    first_name: str
    second_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str
    country: str
    city: str
    created_at: datetime

    class Config:
        orm_mode = True

class HttpResponse(BaseModel):
    status_code: str
    message: str