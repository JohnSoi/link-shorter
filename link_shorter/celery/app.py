"""Модуль экземпляра Celery."""

from celery import Celery

from link_shorter.core import app_config

celery_app: Celery = Celery(
    "statistic",
    broker=app_config.CELERY_BROKER_URL,
    backend=app_config.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
