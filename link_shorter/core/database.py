"""Модуль для работы с базой данных."""

__author__ = "Старков Е.П."

from collections.abc import AsyncGenerator
from datetime import datetime
from typing import Any

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

from .config import app_config

async_engine: AsyncEngine = create_async_engine(app_config.db_url)
async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker[AsyncSession](
    async_engine, expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    """
    Получение асинхронной сессии в контекстном менеджере.

    Returns:
        AsyncGenerator[AsyncSession, Any]: сессия для работы с базой данных.
    """
    async with async_session_maker() as session:
        yield session


Base = declarative_base()


# pylint: disable=too-few-public-methods
class BaseAppModel(Base):
    """
    Базовый класс для моделей приложения.

    Attributes:
        id (int): идентификатор сущности.
        created_at (datetime): дата создания сущности.
    """

    __abstract__: bool = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
