"""Модуль конфига приложения."""

__author__ = "Старков Е.П."

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    """
    Конфиг приложения.

    Attributes:
        DATABASE_HOST (str): хостинг базы данных
        DATABASE_PORT (int): порт базы данных
        DATABASE_NAME (str): имя базы данных
        DATABASE_USER (str): пользователь базы данных
        DATABASE_PASSWORD (str): пароль базы данных
    """
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf8")

    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "link_shorter_db"
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    @property
    def db_url(self) -> str:
        """
        URL подключения к БД через asyncpg.

        Returns:
            str: URL подключения к БД
        """
        return (
            f"postgresql+asyncpg://{self.DATABASE_USER}"
            f":{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}"
            f":{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )


app_config: AppConfig = AppConfig()  # pyright: ignore[reportCallIssue]
