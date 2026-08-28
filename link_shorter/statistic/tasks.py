# pylint: disable=unused-import
"""Celery задачи для статистики."""

__author__ = "Старков Е.П."

import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from link_shorter.celery_app import celery_app
from link_shorter.core import app_config
from link_shorter.shorter.models import ShortLinkModel

from .models import StatisticModel
from .services import StatisticService

# Создаем engine и сессию после импорта моделей
_engine = create_async_engine(app_config.db_url)
_async_session_maker = async_sessionmaker(_engine, class_=AsyncSession)


@celery_app.task
def update_link_statistic(link_id: int) -> None:
    """
    Асинхронное обновление статистики перехода по ссылке.

    Args:
        link_id (int): идентификатор короткой ссылки.
    """

    async def _update() -> None:
        async with _async_session_maker() as session:
            await StatisticService(session).add_use_statistic(link_id)

    asyncio.run(_update())
