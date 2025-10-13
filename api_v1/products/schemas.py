from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str 
    descriptions: str 
    price: int 

class ProductSchema(ProductBase):
    pass

class ProductID(ProductBase):
    id: int