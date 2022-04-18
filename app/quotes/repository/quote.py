from uuid import UUID, uuid4
from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.quotes.models.comment import Comment
from app.quotes.models.detail import Detail
from app.quotes.models.tax import Tax
from app.quotes.models.item import Item
from app.quotes.models.quote import Quote

from app.quotes.schemas.quote_dto import QuoteBase, QuoteCreate, QuoteResponse
from app.common.database import get_db


async def create(quote: QuoteCreate, db: Session = Depends(get_db)) -> QuoteResponse:
    new_quote = Quote(**quote.quote.dict())
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)

    # new_quote.__dict__.update(quote.quote.dict())
    # new_quote.exp_date = quote.quote.exp_date
    # new_quote.quote_status = quote.quote.quote_status
    # new_quote.user_id = quote.quote.user_id
    # new_quote.customer_id = uuid4()

    # new_detail = Detail(**quote.detail.dict())
    # print(new_detail.__dict__)
    # # new_detail.quote_id = new_quote.id
    # db.add(new_detail)
    # db.commit()

    # print(new_detail)
    # new_comment = Comment()
    # new_comment.__dict__.update(quote.comment.dict())

    # new_taxes = [Tax(**tax.dict()) for tax in quote.taxes.taxes]
    # new_items = [Item(**item.dict()) for item in quote.items]
    # print(new_items, new_taxes, new_comment, new_detail, new_quote)

    # db.add_all([new_quote, new_detail, new_comment] + new_taxes + new_items)

    # # new_quote.details = new_detail
    # new_quote.comments = new_comment
    # for item in new_items:
    #     new_quote.items.append(item)
    # for tax in new_taxes:
    #     new_quote.taxes.append(tax)

    # db.refresh(new_quote)
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
