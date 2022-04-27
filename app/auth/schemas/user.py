from pydantic import BaseModel, EmailStr


class LoginResponse(BaseModel):
    message: str
    status: str
    token_type: str
    
class Credentials(BaseModel):
    username: EmailStr
    password: str