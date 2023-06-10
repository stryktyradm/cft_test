import random
import string
from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.core.config import settings
from src.tests.utils.user import create_random_user


def get_user_token_headers(db: Session, client: TestClient) -> Dict[str, str]:
    user, password = create_random_user(db)
    login_data = {
        "username": user.email,
        "password": password
    }
    r = client.post(
        f"{settings.API_V1_STR}/login/access-token", data=login_data
    )
    tokens = r.json()
    access_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    return headers
