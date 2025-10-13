from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Products

from .schemas import ProductSchema

async def get_product(session: AsyncSession) -> list[Products]:
    stmt = select(Products).order_by(Products.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)

async def get_product_by_id(session: AsyncSession, product_id: int) -> Products | None:
    return await session.get(Products, product_id)

async def create_product(session: AsyncSession, new_product: ProductSchema) -> Products:
    product = Products(**new_product.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product