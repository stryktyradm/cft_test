from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.core.config import settings
from src.tests.utils.user import create_random_user


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
