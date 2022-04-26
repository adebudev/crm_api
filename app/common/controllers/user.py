from fastapi import status, Depends, APIRouter
from app.common.schemas.user import UserResponse, UserResponseEmail
from app.common.repository.user import create, getById, send_email, update_password

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserResponse = Depends(create)):
    return user


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
def get_user(user: UserResponse = Depends(getById)):
    return user


@router.post('/send-email', status_code=status.HTTP_200_OK, response_model=UserResponseEmail)
async def send_email_asynchronous(user_email: UserResponseEmail = Depends(send_email)):
    return user_email


@router.put('/reset-password/{id}', status_code=status.HTTP_200_OK, response_model=UserResponse)
def new_password(user: UserResponse = Depends(update_password)):
    return user