from fastapi import APIRouter, Depends

from src import models, schemas
from src.api.deps import current_user_from_token

router = APIRouter()


@router.get("/", response_model=schemas.Salary)
def show_user_salary(
    current_user: models.User = Depends(current_user_from_token)
):
    return current_user.salary
