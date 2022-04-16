from uuid import UUID
from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.quote.schemas.item_dto import ItemCreate, ItemResponse
from app.quote.models.item import Item
from app.common.postgres_conector import get_db_session


async def create(
    item: ItemCreate, db: Session = Depends(get_db_session)
) -> ItemResponse:
    new_item = Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    db.close()
    return new_item


async def get_all(db: Session = Depends(get_db_session)):
    return db.query(Item).all()


async def update(update: ItemCreate, id: UUID, db: Session = Depends(get_db_session)):
    item = db.query(Item).filter(Item.id == id).one_or_none()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quote with id: {} does not exist".format(id),
        )

    for var, value in vars(item).items():
        setattr(item, var, value) if value else None

    item.quantity = update.quantity
    item.unit_value = update.unit_value
    item.description = update.description
    item.item_name = update.item_name
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


async def delete(id: UUID, db: Session = Depends(get_db_session)):
    item = db.query(Item).filter(Item.id == id).one_or_none()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quote with id: {} does not exist".format(id),
        )

    db.delete(item)
    db.commit()
    db.close()
    return JSONResponse(
        content={
            "status_code": status.HTTP_200_OK,
            "message": "item delete successfully",
        }
    )
