from typing import List
from fastapi import Depends, APIRouter, status

from app.common.schemas.item import ItemResponse, HttpResponse
from app.common.services.item import create, get_all, update, delete

router = APIRouter(prefix="/items", tags=["Item"])


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
async def create_item(item = Depends(create)):
    return item

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ItemResponse])
async def get_items(items = Depends(get_all)):
    return items

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=ItemResponse)
async def update_item(item = Depends(update)):
    return item

@router.delete('/{id}', status_code=status.HTTP_200_OK, response_model=HttpResponse)
async def delete_item(response = Depends(delete)):
    return response