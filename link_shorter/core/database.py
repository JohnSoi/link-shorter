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
    async_engine, expire_on_commit=False, class_=AsyncSession
)


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    """
    Получение асинхронной сессии в контекстном менеджере.

    Returns:
        AsyncGenerator[AsyncSession, Any]: сессия для работы с базой данных.

    Examples:
            >>> from fastapi import APIRouter, Depends
            >>> from sqlalchemy.ext.asyncio import AsyncSession
            >>> from link_shorter.core import get_async_session
            >>>
            >>> router: APIRouter = APIRouter("/")
            >>>
            >>> @router.get("/")
            >>> async def example(async_db_session: AsyncSession = Depends(get_async_session)) -> str:
            ...     return "Hello World!"
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

    Examples:
        >>> from sqlalchemy import String
        >>> from sqlalchemy.orm import Mapped, mapped_column
        >>> from link_shorter.core import BaseAppModel
        >>>
        >>>
        >>> # Таблица users с полями name, id, created_at
        >>> class UserModel(BaseAppModel):
        ...    __tablename__: str = "users"
        ...    name: Mapped[str] = mapped_column(String(255))
    """

    __abstract__: bool = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
