"""Модуль маршрутов пакета."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from link_shorter.core import get_async_session

from .consts import PATH_PREFIX
from .schemas import ShorterInputData
from .services import ShortLinkService

shorter_router: APIRouter = APIRouter(prefix=f"/{PATH_PREFIX}", tags=["Links"])


@shorter_router.post("/short", description="Создание короткой ссылки по переданной")
async def short_url(payload: ShorterInputData, async_db_session: AsyncSession = Depends(get_async_session)) -> str:
    """Создание короткой ссылки."""
    return await ShortLinkService(async_db_session).short(str(payload.url))


@shorter_router.get("/{token:str}", description="Переход по короткой ссылке")
async def get_full_url(token: str, async_db_session: AsyncSession = Depends(get_async_session)) -> str:
    """Получение полного URL по токену кроткой ссылки."""
    return await ShortLinkService(async_db_session).get_url(token)
