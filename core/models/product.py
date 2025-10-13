from sqlalchemy.orm import Mapped

from .base import Base

class Products(Base):
    name: Mapped[str]
    descriptions: Mapped[str]
    price: Mapped[int]