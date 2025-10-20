from sqlalchemy.orm import Mapped

from .base import Base

class Users(Base):
    __abstract__ = True
    
    username: Mapped[str]
    name: Mapped[str]
    surname: Mapped[str]
    
    email: ...