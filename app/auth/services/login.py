from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.common.database import get_db
from app.common.models.user import User
from app.auth.schemas.user import Credentials
from app.auth.services.oauth2 import create_access_token

def login_user(user_credentials: Credentials, db: Session = Depends(get_db)) -> str:
    user = db.query(User).filter(User.email == user_credentials.username).one_or_none()
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