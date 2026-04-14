from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserLogin
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(user: UserCreate):
    return await register_user(user)


@router.post("/login")
async def login(user: UserLogin):
    return await login_user(user)