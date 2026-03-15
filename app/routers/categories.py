from fastapi import APIRouter, Depends

from app.schemas.category import CategoryCreate
from app.services.category_service import CategoryService
from app.dependencies.container import get_category_service

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/")
def create_category(
    category: CategoryCreate,
    service: CategoryService = Depends(get_category_service)
):
    return service.create_category(category)


@router.get("/")
def get_categories(
    service: CategoryService = Depends(get_category_service)
):
    return service.get_categories()