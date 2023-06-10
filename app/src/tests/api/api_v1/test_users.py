from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src import crud
from src.core.config import settings
from src.schemas import UserCreate
from src.tests.utils.user import random_email, random_lower_string


def test_create_user_new_email_and_username(
        client: TestClient, db: Session
) -> None:
    email = random_email()
    username = random_lower_string()
    password = random_lower_string()
    data = {
        "email": email,
        "username": username,
        "password": password
    }
    r = client.post(
        f"{settings.API_V1_STR}/users/", json=data
    )
    assert 200 <= r.status_code < 300
    created_user = r.json()
    user = crud.user.get_by_email_or_username(db=db, email=email, username=username)
    assert user
    assert user.email == created_user["email"]


def test_create_existing_user(
        client: TestClient, db: Session
) -> None:
    email = random_email()
    username = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(
        email=email,
        username=username,
        password=password
    )
    crud.user.create_user(db, obj_in=user_in)
    data = {
        "email": email,
        "username": username,
        "password": password
    }
    r = client.post(
        f"{settings.API_V1_STR}/users/", json=data
    )
    created_user = r.json()
    assert r.status_code == 400
    assert "_id" not in created_user
