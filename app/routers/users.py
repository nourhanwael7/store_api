from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate
from app.services.user_service import UserService
from app.dependencies.container import get_user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return service.create_user(user)