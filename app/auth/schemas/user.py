from pydantic import BaseModel, EmailStr


class UserLogIn(BaseModel):
    email: EmailStr
    password: str
