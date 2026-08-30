FROM python:3.12-slim

WORKDIR /app

# Установка uv, системных зависимостей и netcat
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://astral.sh/uv/install.sh | sh

# Установка зависимостей через uv
ENV PATH="/root/.local/bin:$PATH"
COPY pyproject.toml .
RUN uv sync --no-dev

# Копирование исходного кода и entrypoint
COPY ./link_shorter ./link_shorter
COPY ./migration ./migration
COPY ./main.py ./main.py
COPY ./.env ./.env
COPY ./alembic.ini ./alembic.ini
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Порт для FastAPI
EXPOSE 8000

# Entry point с автоматическими миграциями
ENTRYPOINT ["/entrypoint.sh"]

# Команда запуска
CMD ["uv", "run",  "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
