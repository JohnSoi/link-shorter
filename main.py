from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from link_shorter.shorter import shorter_router

from link_shorter.statistic.event_handlers import *

app: FastAPI = FastAPI(
    version="0.1.0",
    title="LinkShorter",
    description="Сервис для сокращения ссылок"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(shorter_router)