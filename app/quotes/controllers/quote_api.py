from typing import List

from app.quotes.repository.quote import create, delete, get_all, update
from app.quotes.schemas.quote_dto import HttpResponse, QuoteResponse, QuoteResponses
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/quotes", tags=["Quotes"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=QuoteResponse)
async def create_quote(quote: QuoteResponse = Depends(create)):
    return quote


@router.get("/", status_code=status.HTTP_200_OK)
async def get_quotes(quotes: List[QuoteResponses] = Depends(get_all)):
    return quotes


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=QuoteResponse)
async def update_quote(quote: QuoteResponse = Depends(update)):
    return quote


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=HttpResponse)
async def delete_quote(response: HttpResponse = Depends(delete)):
    return response
