from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    name: str 
    descriptions: str 
    price: int 
    