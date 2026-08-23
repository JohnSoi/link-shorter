# pylint: disable=too-few-public-methods
"""Модуль моделей пакета."""

__author__ = "Старков Е.П."

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from link_shorter.core import BaseAppModel

from .consts import TOKEN_LENGTH


class ShortLinkModel(BaseAppModel):
    """
    Модель для таблицы с короткими ссылками.

    Attributes:
        original_link (str): исходный URL.
        token (str): токен для короткой ссылки.
    """

    __tablename__: str = "short_links"

    original_link: Mapped[str] = mapped_column(Text, unique=True)
    token: Mapped[str] = mapped_column(String(TOKEN_LENGTH), unique=True)
