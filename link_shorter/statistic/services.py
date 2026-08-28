"""Сервис для работы со статистикой."""

__author__ = "Старков Е.П."

from sqlalchemy.ext.asyncio import AsyncSession

from .repositories import StatisticRepository


class StatisticService:
    """Сервис для работы со статистикой."""

    def __init__(self, async_db_session: AsyncSession) -> None:
        """
        Инициализация сервиса.

        Args:
            async_db_session (AsyncSession): сессия подключения к базе данных.
        """
        self._async_db_session: AsyncSession = async_db_session
        self._repository: StatisticRepository = StatisticRepository(async_db_session)

    async def add_use_statistic(self, short_link_id: int) -> None:
        """
        Добавление статистики использования ссылки.

        Args:
            short_link_id (int): идентификатор записи короткой ссылки.

        Examples:
            >>> async def main():
            ...    async with AsyncSession() as session:
            ...        service: StatisticService = StatisticService(session)
            ...        # добавление статистики использования 1 короткой ссылки
            ...        await service.add_use_statistic(1)
        """
        await self._repository.add_use_statistic(short_link_id)

    async def get_statistic(self) -> dict[str, int | float]:
        """
        Получение статистики.

        Returns:
            dict[str, int | float]: статистика.
        """
        return await self._repository.get_all_statistic()
