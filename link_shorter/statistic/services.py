from sqlalchemy.ext.asyncio import AsyncSession

from .repositories import StatisticRepository


class StatisticService:
    def __init__(self, async_db_session: AsyncSession) -> None:
        self._async_db_session: AsyncSession = async_db_session
        self._repository: StatisticRepository = StatisticRepository(async_db_session)

    async def add_use_statistic(self, short_link_id: int) -> None:
        await self._repository.add_use_statistic(short_link_id)