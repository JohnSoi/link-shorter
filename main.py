from fastapi import FastAPI

from link_shorter.shorter import shorter_router

app: FastAPI = FastAPI(
    version="0.1.0",
    title="LinkShorter",
    description="Сервис для сокращения ссылок"
)

app.include_router(shorter_router)