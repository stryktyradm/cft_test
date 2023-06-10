from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.core.config import settings


def test_read_salary_info(
        client: TestClient, user_token_headers: dict, db: Session
) -> None:
    r = client.get(
        f"{settings.API_V1_STR}/salary/", headers=user_token_headers
    )
    assert r.status_code == 200
    content = r.json()
    assert content["amount"]
    assert content["update"]
