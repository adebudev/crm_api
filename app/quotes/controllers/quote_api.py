from typing import List
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from app.common.database import get_db

from app.quotes.schemas.quote_dto import QuoteResponse, HttpResponse, QuoteCreate
from app.quotes.repository.quote import create, get_all, update, delete
from app.quotes.models.quote import Quote

router = APIRouter(prefix="/quotes", tags=["Quotes"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=QuoteResponse)
async def create_quote(quote: QuoteCreate, db: Session = Depends(get_db)):
    new_quote = Quote(**quote.dict())
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)
    return new_quote


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[QuoteResponse])
async def get_quotes(quotes=Depends(get_all)):
    return quotes


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=QuoteResponse)
async def update_quote(quote=Depends(update)):
    return quote


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=HttpResponse)
async def delete_quote(response=Depends(delete)):
    return response
