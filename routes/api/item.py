from fastapi import APIRouter, Depends
from models.item import Item
from controllers.api.item import create_item , get_items

router = APIRouter()
@router.post("/item")
async def add_item(item: Item):
    return create_item(item)

@router.get("/items")
async def display_items():
    return get_items()