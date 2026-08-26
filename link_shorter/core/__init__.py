"""Пакет базового функционала приложения."""

__author__ = "Старков Е.П."

from .config import app_config
from .database import BaseAppModel, get_async_session
from .exceptions import BaseAppException, BaseAppNotFoundError
from .event_bus import EventBus
