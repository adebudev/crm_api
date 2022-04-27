from fastapi import APIRouter, Depends, status, Response

from app.auth.schemas.user import LoginResponse
from fastapi.responses import JSONResponse

from app.auth.services.oauth2 import get_current_user
from app.common.models.user import User
from app.auth.repository.auth import login_user

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=LoginResponse)
def login(access_token: str = Depends(login_user)):
    content = {"message": "Login succes",
               "status": status.HTTP_200_OK, "token_type": "Bearer"}
    response: Response
    response = JSONResponse(content=content)
    response.set_cookie(key="access_token", value=access_token)
    return response


# This endpoint will be deleted, just for testing purposes
@router.get("/login/test")
def login_test(current_user: User = Depends(get_current_user)):
    # User needs to be authenticated
    print(current_user)
    return {"detail": "User authorized"}
