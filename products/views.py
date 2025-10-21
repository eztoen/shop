from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import ProductSchema, Product

router = APIRouter(prefix='/products', tags=['Products'])

@router.get('/', response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.get_scoped_session)):
    return await crud.get_products(session=session)

@router.get('/{product_id}', response_model=Product)
async def get_product_by_id(product_id: int, session: AsyncSession = Depends(db_helper.get_scoped_session)):
    product = await crud.get_product_by_id(session=session, product_id=product_id)
    if product is not None:
        return product
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Product not found :('
    )

@router.post('/', response_model=Product)
async def create_product(new_product: ProductSchema, session: AsyncSession = Depends(db_helper.get_scoped_session) ):
    return await crud.create_product(session=session, new_product=new_product)