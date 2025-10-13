from sqlalchemy.orm import Mapped

from .base import Base

class Products(Base):
    __tablename__ = 'products'
    
    name: Mapped[str]
    descriptions: Mapped[str]
    price: Mapped[int]