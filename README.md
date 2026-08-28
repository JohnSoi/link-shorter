# Сервис коротких ссылок


## Описание

Сервис предназначен для создания коротких ссылок и получения исходного URL по короткому токену.

## Особенности

При соблюдении именования файлов с моделями (```models.py```) в пакете они автоматически будут подтянуты в миграцию. 
Отдельный импорт не нужен.

## Полезные команды

* Миграция БД:
```bash
uv run alembic upgrade head 
```

* Создание миграции:
```bash
uv run alembic revision --autogenerate -m "<Комментарий>"
```

* Запуск сервера:
```bash
uv run uvicorn main:app --reload 
```

* Запуск воркера Celery
```bash
uv run celery -A link_shorter.celery_app worker --pool=solo --loglevel=info
```

## Статус тестов
[![Lint](https://github.com/JohnSoi/link-shorter/actions/workflows/lint.yml/badge.svg)](https://github.com/JohnSoi/link-shorter/actions/workflows/lint.yml)