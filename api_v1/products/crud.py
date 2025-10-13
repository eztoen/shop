from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Products

async def get_product(session: AsyncSession) -> list[Products]:
    stmt = select(Products).order_by(Products.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)

