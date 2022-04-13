from typing import Optional
from fastapi import Depends, HTTPException, status, Cookie
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.auth.schemas.token import TokenData
from app.common.database import get_db
from app.common.models.user import User
from app.auth.schemas.user import Credentials
from app.auth.services.oauth2 import create_access_token
from app.common.config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm


def login_user(user_credentials: Credentials, db: Session = Depends(get_db)) -> str:
    user = db.query(User).filter(
        User.email == user_credentials.username).one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.verify_password(user_credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token
    access_token = create_access_token(
        data={"user_id": str(user.id)}
    )
    return access_token


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception

        token_data = TokenData(id=id)  # Validate with schema
    except JWTError:
        raise credentials_exception

    return token_data


def get_access_user(access_token: str = Cookie(None), db: Session = Depends(get_db)):
    print(access_token)
    credentiald_expection = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(access_token, credentiald_expection)
    user = db.query(User).filter(User.id == token.id).one_or_none()

    return user
