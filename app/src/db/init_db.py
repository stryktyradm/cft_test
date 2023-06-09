import datetime
import random

from sqlalchemy.orm import Session

from src import crud, schemas
from src.core.config import settings
from src.db import base


def init_db(db: Session) -> None:
    for email, username, password in zip(settings.EMAIL_TEST_USER,
                                         settings.USERNAME_TEST_USER,
                                         settings.PASSWORD_TEST_USER):
        start_date = datetime.datetime(1970, 1, 1)
        end_date = datetime.datetime.now()
        random_date = start_date + datetime.timedelta(
            seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        user_in = schemas.UserCreate(
            email=email,
            username=username,
            password=password,
        )
        user = crud.user.create_user(db=db, obj_in=user_in)
        salary = schemas.SalaryCreate(
            amount=random.randint(1, 1000000),
            update=random_date,
            user_id=user.id
        )
        crud.salary.create(db=db, obj_in=salary)
