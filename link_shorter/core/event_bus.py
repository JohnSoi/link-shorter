from collections import defaultdict
from inspect import iscoroutinefunction
from typing import Callable, TypeAlias, Coroutine

HandlerType: TypeAlias = Callable[[dict], None | Coroutine]


class EventBus:
    _instance = None
    _handlers: dict[str, list[HandlerType]] = defaultdict(list)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EventBus, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def subscribe(self, event_name: str, callback: HandlerType) -> None:
        self._handlers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: HandlerType) -> None:
        if event_name not in self._handlers:
            return

        self._handlers[event_name].remove(callback)

    def clear(self, event_name: str) -> None:
        if event_name not in self._handlers:
            return

        self._handlers[event_name].clear()

    async def emit(self, event_name: str, params: dict) -> None:
        if event_name not in self._handlers:
            return

        for handler in self._handlers[event_name]:
            if iscoroutinefunction(handler):
                await handler(params)
                return

            handler(params)
