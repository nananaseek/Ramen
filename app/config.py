from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Ramen"
    POSTGRESQL_HOSTNAME: str = "localhost"
    POSTGRESQL_USERNAME: str = "postgres"
    POSTGRESQL_PASSWORD: str = ""
    POSTGRESQL_DATABASE: str = "ramen"


settings = Settings()
