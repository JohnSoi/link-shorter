"""Обработчики событий и подпичики."""

__author__ = "Старков Е.П."

from link_shorter.core import EventBus

from .tasks import update_link_statistic


def add_link_statistic(event_data: dict) -> None:
    """
    Обработчик события использования ссылки — запускает Celery задачу.

    Args:
        event_data (dict): данные события
    """
    link_id: int | None = event_data.get("link_id")

    if not link_id:
        return

    update_link_statistic.delay(link_id)


EventBus().subscribe("short_link_used", add_link_statistic)
