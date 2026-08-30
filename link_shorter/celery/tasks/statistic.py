# pylint: disable=unused-import
"""Celery задачи для статистики."""

__author__ = "Старков Е.П."

import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from link_shorter.celery.app import celery_app
from link_shorter.core import app_config
from link_shorter.shorter import ShortLinkService
from link_shorter.statistic import StatisticService

# Создаем engine и сессию после импорта моделей
_engine: AsyncEngine = create_async_engine(app_config.db_url)
_async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(_engine, class_=AsyncSession)


@celery_app.task
def update_link_statistic(link_id: int) -> None:
    """
    Асинхронное обновление статистики перехода по ссылке.

    Args:
        link_id (int): идентификатор короткой ссылки.
    """

    async def _update() -> None:
        async with _async_session_maker() as session:
            # Если ссылки нет - то и нечего писать
            if not await ShortLinkService(session).get_by_id(link_id):
                return

            await StatisticService(session).add_use_statistic(link_id)

    asyncio.run(_update())
