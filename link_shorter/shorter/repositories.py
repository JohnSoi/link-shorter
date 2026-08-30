"""Модуль репозиториев пакета."""

__author__ = "Старков Е.П."

from sqlalchemy import Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import ShortLinkModel


class ShortLinkRepository:
    """Репозиторий коротких ссылок."""

    _MODEL: type[ShortLinkModel] = ShortLinkModel

    def __init__(self, async_db_session: AsyncSession) -> None:
        """
        Инициализация репозитория.

        Args:
            async_db_session (AsyncSession): сессия подключения к БД.
        """
        self._async_db_session: AsyncSession = async_db_session

    async def get_token_by_url(self, url: str) -> str | None:
        """
        Получение токена по переданной ссылке.

        Args:
            url (str): ссылка.

        Returns:
            str | None: токен, если он есть в БД.
        """
        query: Select = select(self._MODEL).filter_by(original_link=url)
        result: Result[ShortLinkModel] = await self._async_db_session.execute(query)
        data: ShortLinkModel | None = result.scalar_one_or_none()

        if not data:
            return None

        return data.token

    async def get_by_token(self, token: str) -> ShortLinkModel | None:
        """
        Получение данных по короткому токену.

        Args:
            token (str): токен короткой ссылки.

        Returns:
            ShortLinkModel | None: url, если он есть в БД.
        """
        query: Select = select(self._MODEL).filter_by(token=token)
        result: Result[ShortLinkModel] = await self._async_db_session.execute(query)
        data: ShortLinkModel | None = result.scalar_one_or_none()

        if not data:
            return None

        return data

    async def create(self, data: dict) -> ShortLinkModel:
        """
        Создание записи с короткой ссылкой.

        Attributes:
            data (dict): данные новой короткой ссылки.
        """
        new_model: ShortLinkModel = self._MODEL()

        for key, value in data.items():
            if hasattr(new_model, key):
                setattr(new_model, key, value)

        self._async_db_session.add(new_model)
        await self._async_db_session.commit()
        await self._async_db_session.refresh(new_model)

        return new_model

    async def get_by_id(self, link_id: int) -> ShortLinkModel | None:
        """
        Получение данных ссылки по id.

        Args:
            link_id (int): id ссылки.

        Returns:
            ShortLinkModel | None: данные ссылки, если он есть в БД.
        """
        query: Select = select(self._MODEL).filter_by(id=link_id)
        result: Result[ShortLinkModel] = await self._async_db_session.execute(query)

        return result.scalar_one_or_none()
