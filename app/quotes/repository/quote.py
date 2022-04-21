from uuid import UUID, uuid4
from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.quotes.models.comment import Comment
from app.quotes.models.detail import Detail
from app.quotes.models.tax import Tax
from app.quotes.models.item import Item
from app.quotes.models.quote import Quote

from app.quotes.schemas.quote_dto import QuoteCreate, QuoteResponse
from app.common.database import get_db


async def create(quote: QuoteCreate, db: Session = Depends(get_db)) -> QuoteResponse:
    new_quote = Quote(**quote.quote.dict())
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)

    if quote.detail:
        new_detail = Detail(**quote.detail.dict())
        new_detail.quote_id = new_quote.id
        db.add(new_detail)
        db.commit()
        db.refresh(new_detail)

    if quote.item:
        for item in quote.item:
            new_item = Item(**item.dict())
            new_item.quote_id = new_quote.id
            db.add(new_item)
            db.commit()
            db.refresh(new_item)

    if quote.taxes:
        for tax in quote.taxes:
            new_tax = Tax(**tax.dict())
            new_tax.quote_id = new_quote.id
            db.add(new_tax)
            db.commit()
            db.refresh(new_tax)

    if quote.comment:
        new_comment = Comment(**quote.comment.dict())
        new_comment.quote_id = new_quote.id
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)

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
    return JSONResponse(
        content={
            "status_code": status.HTTP_200_OK,
            "message": "quote delete successfully",
        }
    )
