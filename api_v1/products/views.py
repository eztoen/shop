from fastapi import APIRouter, Path

from typing import Annotated

from products.schemas import ProductSchema
from products import crud

router = APIRouter(prefix='/items', tags=['Products'])

@router.post('/')
def add_product(new_product: ProductSchema):
    return crud.create_product(new_product)
    
@router.get('/{product_id}/')
def get_product_by_id(product_id: Annotated[int, Path(ge=0, lt=1_000_000)]):
    return crud.get_product_by_id(product_id)