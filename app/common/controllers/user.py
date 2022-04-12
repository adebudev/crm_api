from typing import List
from uuid import UUID
from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.auth.services.login import get_access_user
from app.common.database import get_db
from app.common.schemas.user import UserCreate, UserResponse, UserUpdate, HttpResponse
from app.common.models.user import User


router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
def get_all_user(user: User = Depends(get_access_user),  db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
def get_user(id: UUID, user: User = Depends(get_access_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with id: {} does not exist".format(id),
        )

    return user


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
def update_user(up_user: UserUpdate, id: UUID, user: User = Depends(get_access_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with id: {} does not exist".format(id),
        )

    for var, value in vars(user).items():
        setattr(user, var, value) if value else None

    user.first_name = up_user.first_name
    user.last_name = up_user.last_name
    user.second_name = up_user.second_name
    user.email = up_user.email
    user.address = up_user.address
    user.phone = up_user.phone
    user.city = up_user.city
    user.country = up_user.country
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=HttpResponse)
def delete_user(id: UUID, user: User = Depends(get_access_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with id: {} does not exist".format(id),
        )
    db.delete(user)
    db.commit()
    db.close()
    return JSONResponse(content={"status_code": status.HTTP_200_OK, "message": "password has been successfully updated"})
