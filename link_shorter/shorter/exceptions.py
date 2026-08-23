"""Модуль исключений пакета."""

__author__ = "Старков Е.П."

from link_shorter.core import BaseAppNotFoundError


class TokenNotFoundError(BaseAppNotFoundError):
    """Исключение, если передан неизвестный токен."""

    _MESSAGE = "Короткий токен не найден"
