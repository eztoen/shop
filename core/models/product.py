from sqlalchemy.orm import Mapped

from .base import Base

class Products(Base):
    id: Mapped[int]
    name: Mapped[str]
    descriptions: Mapped[str]
    price: Mapped[int]