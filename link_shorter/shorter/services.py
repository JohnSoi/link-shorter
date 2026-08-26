"""Сервис для работы с короткими ссылками."""

__author__ = "Старков Е.П."

import random
import string

from sqlalchemy.ext.asyncio import AsyncSession

from link_shorter.core import app_config, EventBus

from .consts import PATH_PREFIX, TOKEN_LENGTH
from .exceptions import TokenNotFoundError
from .repositories import ShortLinkRepository


class ShortLinkService:
    """Сервис для работы с короткими ссылками."""

    def __init__(self, async_db_session: AsyncSession) -> None:
        """
        Инициализация сервиса.

        Args:
            async_db_session (AsyncSession): сессия подключения к базе данных.
        """
        self._async_db_session: AsyncSession = async_db_session
        self._repository: ShortLinkRepository = ShortLinkRepository(async_db_session)

    async def short(self, url: str) -> str:
        """
        Создание короткой ссылки.

        Args:
            url (str): URL для создания короткой ссылки.

        Returns:
            str: короткая ссылка.

        Examples:
            >>> from fastapi import APIRouter, Depends
            >>> from sqlalchemy.ext.asyncio import AsyncSession
            >>> from pydantic import BaseModel
            >>> from link_shorter.core import get_async_session
            >>>
            >>> shorter_router: APIRouter = APIRouter(prefix=f"/{PATH_PREFIX}", tags=["Links"])
            >>>
            >>> class Payload(BaseModel):
            ...   url: str
            >>>
            >>>
            >>> @shorter_router.post("/short", description="Создание короткой ссылки по переданной")
            >>> async def short_url(
            ...     payload: Payload,
            ...     async_db_session: AsyncSession = Depends(get_async_session)
            ... ) -> str:
            ...     return await ShortLinkService(async_db_session).short(str(payload.url))
        """
        if exist_token := await self._repository.get_token_by_url(url):
            return f"{app_config.BASE_URL}/{PATH_PREFIX}/{exist_token}"

        token: str = await self._create_new_token(url)

        return f"{app_config.BASE_URL}/{PATH_PREFIX}/{token}"

    async def get_url(self, token: str) -> str:
        """
        Получение URL по токену.

        Args:
            token (str): токен короткой ссылки.

        Returns:
            str: исходный URL.

        Raises:
             TokenNotFoundError: токен не найден.

        Examples:
            >>> from fastapi import APIRouter, Depends
            >>> from sqlalchemy.ext.asyncio import AsyncSession
            >>> from link_shorter.core import get_async_session
            >>>
            >>> shorter_router: APIRouter = APIRouter(prefix=f"/{PATH_PREFIX}", tags=["Links"])
            >>>
            >>> @shorter_router.get("/{short_token:str}", description="Переход по короткой ссылке")
            >>> async def get_full_url(
            ...     short_token: str,
            ...     async_db_session: AsyncSession = Depends(get_async_session)
            ... ) -> str:
            ...     return await ShortLinkService(async_db_session).get_url(token)
        """
        if token_data := await self._repository.get_by_token(token):
            await EventBus().emit(
                "short_link_used",
                {
                    "link_id": token_data.id,
                    "db_session": self._async_db_session
                }
            )
            return token_data.original_link

        raise TokenNotFoundError()

    async def _create_new_token(self, url: str) -> str:
        """
        Создание нового уникального токена.

        Notes:
            Создается случайный строковый токен длиной TOKEN_LENGTH с проверкой на существование токена в базе данных.
            Если токен существует, то создается новый токен.

        Args:
            url (str): URL для создания нового токена.

        Returns:
            str: новый токен.
        """
        token: str = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(TOKEN_LENGTH))

        if await self._repository.get_url_by_token(token):
            return await self._create_new_token(url)

        await self._repository.create({"original_link": url, "token": token})

        return token
