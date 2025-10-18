from asyncio import current_task

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, async_scoped_session

from core.config import settings


class Base(DeclarativeBase):
    __abstract__ = True
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}'
    
    id: Mapped[int] = mapped_column(primary_key=True)