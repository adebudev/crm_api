from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_password: str
    postgres_port: str
    postgres_user: str
    postgres_db: str
    database_hostname: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    postgres_test_password: str
    postgres_test_user: str
    postgres_test_db: str
    database_test_hostname: str
    postgres_test_port: str

    class Config:
        env_file = "environments/development.env"


settings = Settings()
