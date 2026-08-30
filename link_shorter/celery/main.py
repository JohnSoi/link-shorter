# pylint: disable=wildcard-import, unused-wildcard-import, wrong-import-position, unused-import
"""Инициализация Celery."""

from .app import celery_app  # noqa

# Импорт задач для их регистрации в Celery
from .tasks import *
