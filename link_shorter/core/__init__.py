"""Пакет базового функционала приложения."""

__author__ = "Старков Е.П."

from .config import app_config
from .database import BaseAppModel, async_session_maker
