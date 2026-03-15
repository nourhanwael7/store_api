from fastapi import APIRouter, Depends

from app.schemas.product import ProductCreate
from app.services.product_service import ProductService
from app.dependencies.container import get_product_service

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
def create_product(
    product: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    return service.create_product(product)


@router.get("/")
def get_products(
    skip: int = 0,
    limit: int = 10,
    service: ProductService = Depends(get_product_service)
):
    return service.get_products(skip, limit)