from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf8")

    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "link_shorter_db"
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DATABASE_USER}"
            f":{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}"
            f":{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )


app_config: AppConfig = AppConfig()
