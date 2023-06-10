from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.db.session import SessionLocal
from src.main import app
from src.tests.utils.utils import get_user_token_headers


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def user_token_headers(db: Session, client: TestClient) -> Dict[str, str]:
    return get_user_token_headers(db, client)
