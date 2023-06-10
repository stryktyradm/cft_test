from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.core.config import settings
from src.tests.utils.user import create_random_user, random_email, random_lower_string


def test_get_access_token(db: Session, client: TestClient) -> None:
    user, password = create_random_user(db)
    login_data = {
        "username": user.email,
        "password": password
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


def test_get_access_token_with_incorrect_credential(db: Session, client: TestClient) -> None:
    email = random_email()
    password = random_lower_string()
    login_data = {
        "username": email,
        "password": password
    }
    r = client.post(
        f"{settings.API_V1_STR}/login/access-token", data=login_data
    )
    assert r.status_code == 400


def test_use_access_token(
        client: TestClient, user_token_headers: Dict[str, str]
) -> None:
    r = client.get(
        f"{settings.API_V1_STR}/salary/", headers=user_token_headers
    )
    result = r.json()
    assert r.status_code == 200
    assert "update" in result
