from fastapi import APIRouter, Path

from typing import Annotated

router = APIRouter(prefix='/items', tags=['Products'])

@router.get('/')
def get_all_item():
    return [
        'iPhone 15',
        'iPhone 15 pro',
        'iPhone 15 pro max'
    ]
    
# @router.get('/{product_id}')
# def get_product_by_id(product_id: Annotated[int, Path(ge=0, lt=[1_000_000])]):
#     return {
#         'id': product_id,
#         'product': 'product'
#     }