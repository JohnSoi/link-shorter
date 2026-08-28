# pylint: disable=too-few-public-methods
"""Модуль моделей пакета."""

__author__ = "Старков Е.П."

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from link_shorter.core import BaseAppModel


class StatisticModel(BaseAppModel):
    """
    Модель статистики переходов по ссылке.

    Attributes:
        link_id (int): идентификатор связанной ссылки.
    """

    __tablename__: str = "statistics"

    link_id: Mapped[int] = mapped_column(ForeignKey("short_links.id"))
