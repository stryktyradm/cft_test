import random
import string
from typing import Tuple

from sqlalchemy.orm import Session

from src import crud
from src.models import User
from src.schemas import UserCreate
from src.tests.utils.salary import create_random_salary


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"


def create_random_user(db: Session) -> Tuple[User, str]:
    email = random_email()
    username = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(
        email=email,
        username=username,
        password=password
    )
    user = crud.user.create_user(db=db, obj_in=user_in)
    create_random_salary(db, user)
    return user, password
