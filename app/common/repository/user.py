from datetime import datetime
from uuid import UUID
from fastapi import status, HTTPException, Depends
from fastapi_mail import FastMail, MessageSchema
from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.common.database import get_db
from app.common.schemas.user import UserBase, UserCreate, UserResponse, UserResponseEmail, UserUpdatePassword
from app.common.models.user import User
from fastapi.responses import JSONResponse
from app.config.email_conf import conf


def create(user: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def getById(id: UUID, db: Session = Depends(get_db)) -> UserResponse:
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with id: {} does not exist".format(id),
        )
    return user


async def send_email_async(email_to: EmailStr, body: dict):
    message = MessageSchema(
        subject='Recuperar contraseña',
        recipients=[email_to],
        template_body=body
    )

    fm = FastMail(conf)
    await fm.send_message(message, template_name='email.html')


async def send_email(user_email: UserBase, db: Session = Depends(get_db)) -> UserResponseEmail:
    user: User = db.query(User).filter(
        User.email == user_email.email).one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email not found",
        )
    link = "http://localhost:3000/reset-password/{}".format(str(user.id))
    await send_email_async(user.email,
                           {
                               "title": "PERSONAL CRM",
                               "user_email": user.email,
                               "link": link
                           })
    return JSONResponse(
        content={
            "status_code": status.HTTP_200_OK,
            "message": "send email success",
            "email": user.email
        })


def update_password(user_password: UserUpdatePassword, id: UUID, db: Session = Depends(get_db)) -> UserResponse:
    user: User = db.query(User).filter(User.id == id).one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with id: {} does not exist".format(id),
        )

    for var, value in vars(user).items():
        setattr(user, var, value) if value else None

    user.password = user_password.password
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
