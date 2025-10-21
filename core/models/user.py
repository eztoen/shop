from sqlalchemy.orm import Mapped

from .base import Base

class Users(Base):
    username: Mapped[str]
    name: Mapped[str]
    surname: Mapped[str]