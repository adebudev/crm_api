import json

from app.auth.schemas.user import UserLogIn
from app.auth.services import oauth2
from app.auth.services.oauth2 import get_current_user
from app.common.database import get_db
from app.common.models.user import User
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.verify_password(user_credentials.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token
    access_token = oauth2.create_access_token(
        data={"user_id": json.dumps(str(user.id))}
    )
    # return token
    return {"access_token": access_token, "token_type": "Bearer"}


# This endpoint will be deleted, just for testing purposes
@router.get("/login/test")
def login_test(user_id: str = Depends(get_current_user)):
    # User needs to be authenticated
    print(user_id)
    return {"detail": "User authorized"}
