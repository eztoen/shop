from fastapi import APIRouter, Path, HTTPException, status

from . import crud
from .schemas import ProductSchema, Product

router = APIRouter(prefix='/products', tags=['Products'])

@router.get('/', response_model=list[Product])
async def get_products(session):
    return await crud.get_products(session=session)

@router.get('/{product_id}', response_model=Product)
async def get_product_by_id(product_id: int, session):
    product = await crud.get_product_by_id(session=session, product_id=product_id)
    if product is not None:
        return product
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Product not found :('
    )

@router.post('/', response_model=Product)
async def create_product(session, new_product: ProductSchema):
    return await crud,create_product(session=session, new_product=new_product)