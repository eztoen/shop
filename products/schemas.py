from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name: str 
    descriptions: str 
    price: int 

class ProductSchema(ProductBase):
    pass

class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int