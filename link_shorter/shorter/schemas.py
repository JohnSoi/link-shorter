"""Модуль схем данных пакета."""

__author__ = "Старков Е.П."

from pydantic import BaseModel, HttpUrl


class ShorterInputData(BaseModel):
    """
    Входные данные для сокращения URL.

    Attributes:
        url (HttpUrl): URL для сокращения.
    """

    url: HttpUrl
