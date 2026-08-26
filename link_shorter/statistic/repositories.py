from sqlalchemy.ext.asyncio import AsyncSession

from .models import StatisticModel

class StatisticRepository:
    _MODEL: type[StatisticModel] = StatisticModel

    def __init__(self, async_db_session: AsyncSession) -> None:
        """
        Инициализация репозитория.

        Args:
            async_db_session (AsyncSession): сессия подключения к БД.
        """
        self._async_db_session: AsyncSession = async_db_session

    async def add_use_statistic(self, short_link_id: int) -> None:
        new_model: StatisticModel = StatisticModel(link_id=short_link_id)

        self._async_db_session.add(new_model)
        await self._async_db_session.commit()
