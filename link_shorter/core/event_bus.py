"""Модуль шины событий приложения."""

__author__ = "Старков Е.П."

from collections import defaultdict
from collections.abc import Callable, Coroutine
from inspect import iscoroutinefunction
from typing import ClassVar

# Тип обработчиков события
type HandlerType = Callable[[dict], None | Coroutine]


class EventBus:
    """
    Шина событий приложения.

    Attributes:
        _instance (EventBus): экземпляр шины событий для синглтона
        _handlers (dict[str, list[HandlerType]]): словарь обработчиков событий
    """

    _instance = None
    _handlers: ClassVar[dict[str, list[HandlerType]]] = defaultdict(list)

    def __new__(cls, *args, **kwargs):
        """Поддержка паттерна синглтона."""
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def subscribe(self, event_name: str, callback: HandlerType) -> None:
        """
        Подписка на событие.

        Args:
            event_name (str): название события
            callback (HandlerType): обработчик события

        Examples:
            >>> from link_shorter.core import EventBus
            >>> # Обработка события event. Обработчик обязательно принимает аргумент
            >>> EventBus().subscribe("event", lambda params: print(params))
        """
        self._handlers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: HandlerType) -> None:
        """
        Отписка от события. Если такой обработчик не был подписан, ничего не делает.

        Args:
            event_name (str): название события
            callback (HandlerType): обработчик события для удаления

        Examples:
            >>> from link_shorter.core import EventBus
            >>> # Обработка события event. Обработчик обязательно принимает аргумент
            >>> EventBus().subscribe("event", lambda params: print(params))
            >>> # Удаляет ранее добавленный обработчик
            >>> EventBus().unsubscribe("event", lambda params: print(params))
            >>> # Не упадет, так как обработчик не был подписан
            >>> EventBus().unsubscribe("event", lambda params: print(123))
            >>> # Не упадет, так как обработчик нет такого события
            >>> EventBus().unsubscribe("wrong_event", lambda params: print(params))
        """
        if event_name not in self._handlers or callback not in self._handlers[event_name]:
            return

        self._handlers[event_name].remove(callback)

    def clear(self, event_name: str) -> None:
        """
        Полностью очищает обработчики определенного события.

        Args:
            event_name (str): название события

        Examples:
            >>> from link_shorter.core import EventBus
            >>> # Обработка события event. Обработчик обязательно принимает аргумент
            >>> EventBus().subscribe("event", lambda params: print(params))
            >>> # Обработка события event. Обработчик обязательно принимает аргумент
            >>> EventBus().unsubscribe("event", lambda params: print(123))
            >>> # Очищает все обработчики события event
            >>> EventBus().clear("event")
            >>> # Не упадет, так как просто ничего не очищает
            >>> EventBus().clear("wrong_event")
        """
        if event_name not in self._handlers:
            return

        self._handlers[event_name].clear()

    async def emit(self, event_name: str, params: dict) -> None:
        """
        Отправка и обработка событий. Выполняется асинхронно.

        Args:
            event_name (str): название события
            params (dict): параметры события

        Examples:
            >>> from link_shorter.core import EventBus
            >>> # Обработка события event. Обработчик обязательно принимает аргумент
            >>> EventBus().subscribe("event", lambda event_params: print(event_params))
            >>>
            >>> async def main() -> None:
            ...     # Выведет в консоль {"message": "Hello, world!"}
            ...     await EventBus().emit("event", {"message": "Hello, world!"})
        """
        if event_name not in self._handlers:
            return

        for handler in self._handlers[event_name]:
            if iscoroutinefunction(handler):
                await handler(params)
                return

            handler(params)
