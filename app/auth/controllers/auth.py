from fastapi import APIRouter, Depends, Response, status, Cookie
from fastapi.responses import JSONResponse

from app.auth.schemas.token import Token
from app.auth.schemas.user import UserLogIn
from app.common.models.user import User
from app.auth.services.oauth2 import authentication_user, get_current_user
from app.auth.services.login import get_access_user, login_user

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=UserLogIn)
def login(access_token: str = Depends(login_user)):
    content = {"message": "Login succes",
               "status": status.HTTP_200_OK, "token_type": "Bearer"}
    response: Response
    response = JSONResponse(content=content)
    response.set_cookie(key="access_token", value=access_token)
    return response

@router.get("/login/test")
def login_test(current_user: User = Depends(get_access_user)):
    # User needs to be authenticated
    print(current_user)
    return {"detail": "User authorized"}


@router.get("/token/test")
def login_test(current_user: User = Depends(get_current_user)):
    # User needs to be authenticated
    print(current_user)
    return {"detail": "User authorized"}


@router.post("/token", response_model=Token)
def login(access_token: str = Depends(authentication_user)):
    return {"access_token": access_token, "token_type": "bearer"}
