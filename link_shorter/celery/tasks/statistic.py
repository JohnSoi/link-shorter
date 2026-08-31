# pylint: disable=unused-import
"""Celery задачи для статистики."""

__author__ = "Старков Е.П."

import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import NullPool

from link_shorter.celery.app import celery_app
from link_shorter.core import app_config
from link_shorter.shorter import ShortLinkService
from link_shorter.statistic import StatisticService


@celery_app.task
def update_link_statistic(link_id: int) -> None:
    """
    Асинхронное обновление статистики перехода по ссылке.

    Notes:
        Каждый вызов создаёт собственный AsyncEngine и session maker,
        чтобы полностью изолировать контекст БД от других задач Celery.
        Это исключает ошибку "another operation is in progress", когда
        несколько воркеров параллельно выполняют асинхронные запросы.

    Args:
        link_id (int): идентификатор короткой ссылки.
    """

    def _run() -> None:
        """Создаём новый event loop + engine для каждой задачи."""

        async def _update() -> None:
            engine = create_async_engine(app_config.db_url, poolclass=NullPool)
            try:
                async with (
                    engine.connect() as conn,
                    AsyncSession(bind=conn, expire_on_commit=False) as session,
                ):
                    # Если ссылки нет - то и нечего писать
                    if not await ShortLinkService(session).get_by_id(link_id):
                        return

                    await StatisticService(session).add_use_statistic(link_id)
            finally:
                await engine.dispose()

        asyncio.run(_update())

    _run()
