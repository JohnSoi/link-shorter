from sqlalchemy.ext.asyncio import AsyncSession

from .services import StatisticService
from link_shorter.core import EventBus


async def add_link_statistic(event_data: dict) -> None:
    session_data: AsyncSession | None = event_data.get("db_session")
    link_id: int | None = event_data.get("link_id")

    if not session_data or not link_id:
        return

    await StatisticService(session_data).add_use_statistic(link_id)


EventBus().subscribe("short_link_used", add_link_statistic)