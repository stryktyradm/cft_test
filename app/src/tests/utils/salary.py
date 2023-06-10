import random
import datetime
from datetime import date

from sqlalchemy.orm import Session

from src import crud
from src.models import User
from src.schemas import SalaryCreate


def random_datetime() -> date:
    start_date = datetime.datetime(1970, 1, 1)
    end_date = datetime.datetime.now()
    random_date = start_date + datetime.timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date


def create_random_salary(db: Session, user: User) -> None:
    amount = random.randint(1, 100000)
    random_date = random_datetime()
    user_id = user.id
    salary = SalaryCreate(
        amount=amount,
        update=random_date,
        user_id=user_id
    )
    crud.salary.create(db, obj_in=salary)
