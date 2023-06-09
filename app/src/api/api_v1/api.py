from fastapi import APIRouter

from src.api.api_v1.endpoints import users, login, salaryinfo

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(salaryinfo.router, prefix="/salary", tags=["salary"])
