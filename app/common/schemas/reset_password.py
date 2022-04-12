from email import message
import email
from pydantic import BaseModel, EmailStr


class Email(BaseModel):
    email: EmailStr
    
class SendEmail(BaseModel):
    status_code: str
    message: str
    email: str
    
class ResetPassword(BaseModel):
    new_password: str
    confirm_password: str
    
class HttpResponse(BaseModel):
    status_code: str
    message: str