from typing import List
from uuid import UUID

from app.auth.repository.auth import get_access_user
from app.common.database import get_db
from app.common.models.client import Client
from app.common.schemas.client import ClientCreate, ClientResponse
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/client", tags=["Clients"])


# TODO: protect route with credentials
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClientResponse)
async def create_client(client: ClientCreate, db: Session = Depends(get_db), access = Depends(get_access_user)):
    new_client = Client(**client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=List[ClientResponse])
async def get_clients(user_id: UUID, db: Session = Depends(get_db), access = Depends(get_access_user)):
    return db.query(Client).filter(Client.user_id == user_id).all()
