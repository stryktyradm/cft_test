import secrets
from typing import Optional, Dict, Any, List, Union

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    PROJECT_NAME: str
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn]
    EMAIL_TEST_USER: Union[str, List[str]]
    USERNAME_TEST_USER: Union[str, List[str]]
    PASSWORD_TEST_USER: Union[str, List[str]]

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            return v
        postgres_uri = PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}"
        )
        return postgres_uri

    @validator("EMAIL_TEST_USER", pre=True)
    def split_email_list(cls, v: Optional[str]):
        if isinstance(v, str):
            return v.split(',')
        return v

    @validator("USERNAME_TEST_USER", pre=True)
    def split_username_list(cls, v: Optional[str]):
        if isinstance(v, str):
            return v.split(',')
        return v

    @validator("PASSWORD_TEST_USER", pre=True)
    def split_password_list(cls, v: Optional[str]):
        if isinstance(v, str):
            return v.split(',')
        return v

    class Config:
        # env_file = "test_env_vars.sh"
        case_sensitive = True


settings = Settings()
