from uuid import UUID
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.common.models.user import User
from app.common.schemas.reset_password import Email, HttpResponse, SendEmail, ResetPassword
from app.common.database import get_db
from app.config.email_config import conf

router = APIRouter(prefix="/user", tags=["Reset Password"])


async def send_email_async(email_to: EmailStr, body: dict):
    message = MessageSchema(
        subject='Recuperar contraseña',
        recipients=[email_to],
        template_body=body
    )

    fm = FastMail(conf)
    await fm.send_message(message, template_name='email.html')


@router.post('/send-email', status_code=status.HTTP_200_OK, response_model=SendEmail)
async def send_email_asynchronous(user_email: Email, db: Session = Depends(get_db)) -> SendEmail:
    user: User = db.query(User).filter(
        User.email == user_email.email).one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email not found",
        )
    link = "http://localhost:8000/user/new-password/{}".format(str(user.id))
    await send_email_async(user.email,
                           {
                               "title": "PERSONAL CRM",
                               "user_email": user.email,
                               "link": link
                           })
    return JSONResponse(content={"status_code": status.HTTP_200_OK, "message": "send email success", "email": user.email})


@router.put('/new-password/{id}', status_code=status.HTTP_200_OK, response_model=HttpResponse)
async def new_password_user(password: ResetPassword, id: UUID, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with id: {} does not exist".format(id),
        )
    if password.new_password != password.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The password do not match",
        )

    for var, value in vars(user).items():
        setattr(user, var, value) if value else None

    user.password = password.new_password
    db.add(user)
    db.commit()
    db.refresh(user)
    return JSONResponse(content={"status_code": status.HTTP_200_OK, "message": "password has been successfully updated"})
