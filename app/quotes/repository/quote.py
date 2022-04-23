import datetime
from uuid import UUID

from app.common.database import get_db
from app.quotes.models.comment import Comment
from app.quotes.models.detail import Detail
from app.quotes.models.item import Item
from app.quotes.models.quote import Quote
from app.quotes.models.tax import Tax
from app.quotes.schemas.quote_dto import (
    QuoteCreate,
    QuoteResponse,
    QuoteResponses,
    QuoteUpdate,
)
from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List


async def create(quote: QuoteCreate, db: Session = Depends(get_db)) -> QuoteResponse:
    # TODO: quote_num -> user_id
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


async def get_all(db: Session = Depends(get_db)) -> List[QuoteResponses]:
    return db.query(Quote).all()


async def update(update_post: QuoteUpdate, id: UUID, db: Session = Depends(get_db)):
    quote_query = db.query(Quote).filter(Quote.id == id)
    quote = quote_query.first()
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote with id: {} does not exist".format(id),
        )

    if update_post.client_id != quote.client_id or update_post.user_id != quote.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action",
        )

    quote_query.update(update_post.dict(), synchronize_session=False)
    quote.modified_on = datetime.datetime.now()
    db.commit()
    return quote_query.first()


async def delete(id: UUID, db: Session = Depends(get_db)):
    quote_query = db.query(Quote).filter(Quote.id == id)
    quote = quote_query.first()
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote with id: {} does not exist".format(id),
        )

    quote_query.delete(synchronize_session=False)
    db.commit()
    return JSONResponse(
        content={
            "status_code": status.HTTP_200_OK,
            "message": "quote delete successfully",
        }
    )
