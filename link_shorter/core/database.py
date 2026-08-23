from datetime import datetime
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

from .config import app_config


async_engine: AsyncEngine = create_async_engine(app_config.db_url)
async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker[AsyncSession](
    async_engine,
    expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    async with async_session_maker() as session:
        yield session


Base = declarative_base()


class BaseAppModel(Base):
    __abstract__: bool = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
