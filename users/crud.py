from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Users

async def get_users(session: AsyncSession) -> list[Users]:
    stmt = select(Users).order_by(Users.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)

async def get_user_by_id(session: AsyncSession, user_id: int) -> Users | None:
    return await session.get(Users, user_id)