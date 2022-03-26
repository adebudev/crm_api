from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_password: str
    postgres_port: str
    postgres_user: str
    postgres_db: str
    database_hostname: str

    class Config:
        env_file = "environments/development.env"


settings = Settings()
