from fastapi import status, APIRouter
from starlette.responses import JSONResponse

from app.common.controllers.auth.password.reset import send_email

router = APIRouter(prefix="/auth", tags=["Reset Password"])

router.include_router(send_email.router)

@router.get('/')
def reset_password():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "reset password"})