from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Products

async def get_product(session: AsyncSession) -> list[Products]:
    stmt = select(Products).order_by(Products.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)

async def get_product_by_id(product_id: int, session: AsyncSession) -> Products | None:
    return await session.get(Products, product_id)