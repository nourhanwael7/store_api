from pydantic import BaseModel


class ProductCreate(BaseModel):
    product_name: str
    price: float
    category_id: int
    user_id: int


class ProductResponse(BaseModel):
    id: int
    product_name: str
    price: float
    category_id: int
    user_id: int

    class Config:
        from_attributes = True