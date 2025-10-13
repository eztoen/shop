from typing import Annotated

from fastapi import Path
from products.schemas import ProductSchema

def create_product(product: ProductSchema) -> dict:
    product = product.model_dump()
    return {
        'success': True,
        'product': product,
    }
    
def get_product_by_id(id: Annotated[int, Path(ge=1, lt=1_000_000)]) -> dict:
    return {
        'id': id,
        'product': 'product'
    }