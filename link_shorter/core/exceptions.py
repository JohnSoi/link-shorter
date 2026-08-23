"""Модуль базовых исключений приложения."""

__author__ = "Старков Е.П."

from fastapi import HTTPException, status


class BaseAppException(HTTPException):
    """
    Базовое исключение приложения.

    Attributes:
        _CODE (int): код ошибки. Лучше из from fastapi import status
        _MESSAGE (str): сообщение ошибки.

    Examples:
        >>> from link_shorter.core import BaseAppException
        >>>
        >>>
        >>> class BadError(BaseAppException):
        ...    _MESSAGE = "Стало плохо("
        >>>
        >>>
        >>> class BadRequestError(BaseAppException):
        ...     _CODE = status.HTTP_400_BAD_REQUEST
        ...     _MESSAGE = "Неверный запрос"
    """

    _CODE: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    _MESSAGE: str = "Внутренняя ошибка сервера"

    def __init__(self) -> None:
        super().__init__(detail=self._MESSAGE, status_code=self._CODE)


class BaseAppNotFoundError(BaseAppException):
    """
    Базовое исключение ненайденного ресурса.

    Examples:
        >>> from link_shorter.core import BaseAppException
        >>>
        >>>
        >>> class BadError(BaseAppException):
        >>>    _MESSAGE = "Стало плохо("
    """

    _CODE: int = status.HTTP_404_NOT_FOUND
    _MESSAGE: str = "Запрашиваемый ресурс не найден"
