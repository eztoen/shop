from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    name: str = Field(..., max_length=200)
    price: int = Field(..., description='Rubles')
    descriptions: str = Field(..., max_length=3000)