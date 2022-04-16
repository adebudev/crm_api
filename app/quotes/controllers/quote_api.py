from typing import List
from fastapi import Depends, APIRouter, status

from app.quotes.schemas.quote_dto import QuoteResponse, HttpResponse, QuoteCreate
from app.quotes.repository.quote import create, get_all, update, delete

router = APIRouter(prefix="/quotes", tags=["Quotes"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=str)
async def create_quote(quote: QuoteCreate = Depends(create)):
    return quote


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[QuoteResponse])
async def get_quotes(quotes=Depends(get_all)):
    return quotes


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=QuoteResponse)
async def update_quote(quote=Depends(update)):
    return quote


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=HttpResponse)
async def delete_quote(response=Depends(delete)):
    return response
