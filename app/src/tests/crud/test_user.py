from sqlalchemy.orm import Session

from src import crud
from src.schemas import UserCreate
from src.tests.utils.user import random_email, random_lower_string


def test_get_user_from_email_or_username(db: Session) -> None:
    email = random_email()
    username = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(
        email=email,
        username=username,
        password=password
    )
    user = crud.user.create_user(db, obj_in=user_in)
    get_user = crud.user.get_by_email_or_username(db, email=email, username=username)
    assert user.email == get_user.email
    assert user.username == get_user.username


def test_not_get_user_from_email_or_username(db: Session) -> None:
    email = random_email()
    username = random_lower_string()
    user = crud.user.get_by_email_or_username(db, email=email, username=username)
    assert user is None


def test_create_user(db: Session) -> None:
    email = random_email()
    username = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(
        email=email,
        username=username,
        password=password
    )
    user = crud.user.create_user(db, obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "hashed_password")


def test_authenticate_user(db: Session) -> None:
    email = random_email()
    username = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(
        email=email,
        username=username,
        password=password
    )
    user = crud.user.create_user(db, obj_in=user_in)
    authenticated_user = crud.user.authenticate(
        db=db,
        username=user.email,
        password=password
    )
    assert authenticated_user
    assert user.email == authenticated_user.email


def test_not_authenticate_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user = crud.user.authenticate(db=db, username=email, password=password)
    assert user is None
