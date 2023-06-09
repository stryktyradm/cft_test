from typing import Generator

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from jose import jwt

from src.db.session import SessionLocal
from src import models, schemas, crud
from src.core import security
from src.core.config import settings


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def current_user_from_token(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> models.User:
    credential_exception = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials."
        )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=security.ALGORITHM
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValueError):
        raise credential_exception
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise credential_exception
    return user
