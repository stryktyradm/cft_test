from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import schemas, crud
from src.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.UserCreate
):
    '''

    :param db:
    :param user_in:
    :return:
    '''
    user = crud.user.get_by_email_or_username(
        db=db,
        email=user_in.email,
        username=user_in.username
    )
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username or email already exists in the system."
        )
    user = crud.user.create_user(db, obj_in=user_in)
    return user
