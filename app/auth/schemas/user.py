from pydantic import BaseModel, EmailStr


class UserLogIn(BaseModel):
    message: str
    status: str
    token_type: str
    
class Credentials(BaseModel):
    username: EmailStr
    password: str