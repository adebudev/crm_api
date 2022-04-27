from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserBase(BaseModel):
    first_name: str
    second_name: Optional[str]
    last_name: str
    email: EmailStr
    phone: str
    address: str
    country: Optional[str]
    city: Optional[str]

class UserCreate(UserBase):
    password: str

class UserUpdatePassword(BaseModel):
    password: str

class UserResponse(UserBase):
    id: UUID
    created_at: datetime = Field(..., alias="createdAt")

    class Config:
        orm_mode = True

class UserEmail(BaseModel):
    email: EmailStr

class UserResponseEmail(UserEmail):
    status_code: int
    message: str