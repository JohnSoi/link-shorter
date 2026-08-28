"""Модуль репозиториев пакета."""

__author__ = "Старков Е.П."

from sqlalchemy import ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from .models import StatisticModel


class StatisticRepository:
    """Репозиторий статистики."""

    _MODEL: type[StatisticModel] = StatisticModel

    def __init__(self, async_db_session: AsyncSession) -> None:
        """
        Инициализация репозитория.

        Args:
            async_db_session (AsyncSession): сессия подключения к БД.
        """
        self._async_db_session: AsyncSession = async_db_session

    async def add_use_statistic(self, short_link_id: int) -> None:
        """
        Добавление статистки использования короткого токена.

        Args:
            short_link_id (int): идентификатор записи с короткой ссылкой.

        Examples:
            >>> async def main():
            ...    async with AsyncSession() as session:
            ...        repository: StatisticRepository = StatisticRepository(session)
            ...        # добавление статистики использования 1 короткой ссылки
            ...        await repository.add_use_statistic(1)
        """
        new_model: StatisticModel = StatisticModel(link_id=short_link_id)

        self._async_db_session.add(new_model)
        await self._async_db_session.commit()

    async def get_all_statistic(self) -> dict[str, int | float]:
        """
        Получение статистики использования шортера.

        Returns:
            dict[str, int | float]: статистика использования коротких ссылок.
        """
        all_statistic: ScalarResult[list[StatisticModel]] = await self._async_db_session.scalars(self._MODEL.select())

        return {
            "all_links": all_statistic.fetchall().count(1),
        }
