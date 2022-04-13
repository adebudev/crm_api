from uuid import UUID
from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.common.schemas.quote import QuoteCreate, QuoteResponse
from app.common.models.quote import Quote
from app.common.database import get_db


async def create(quote: QuoteCreate, db: Session = Depends(get_db)) -> QuoteResponse:
    new_quote = Quote(**quote.dict())
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)
    return new_quote

async def get_all(db: Session = Depends(get_db)):
    return db.query(Quote).all()

async def update(update: QuoteCreate, id: UUID, db: Session = Depends(get_db)):
    quote = db.query(Quote).filter(Quote.id == id).one_or_none()
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quote with id: {} does not exist".format(id),
        )

    for var, value in vars(quote).items():
        setattr(quote, var, value) if value else None
        
    quote.quote_num = update.quote_num
    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote

async def delete(id: UUID, db: Session = Depends(get_db)):
    quote = db.query(Quote).filter(Quote.id == id).one_or_none()
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quote with id: {} does not exist".format(id),
        )
        
    db.delete(quote)
    db.commit()
    db.close()
    return JSONResponse(content={"status_code": status.HTTP_200_OK, "message": "quote delete successfully"})
