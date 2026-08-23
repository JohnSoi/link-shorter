from fastapi import FastAPI

app: FastAPI = FastAPI(
    version="0.1.0",
    title="LinkShorter",
    description="Сервис для сокращения ссылок"
)
