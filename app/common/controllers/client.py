from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.common.database import get_db
from app.common.schemas.client import ClientResponse, ClientCreate
from app.common.models.client import Client

router = APIRouter(prefix="/client", tags=["Clients"])


# TODO: protect route with credentials
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClientResponse)
async def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    new_client = Client(**client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client
