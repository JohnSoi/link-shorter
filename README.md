# Сервис коротких ссылок


## Описание

Сервис предназначен для создания коротких ссылок и получения исходного URL по короткому токену.

## Особенности

При соблюдении именования файлов с моделями (```models.py```) в пакете они автоматически будут подтянуты в миграцию. 
Отдельный импорт не нужен.

## Полезные команды

* Миграция БД:
```bash
alembic upgrade head 
```

* Создание миграции:
```bash
alembic revision --autogenerate -m "<Комментарий>"
```

* Запуск сервера:
```bash
uv run uvicor main:app --reload 
```

## Статус тестов
[![Lint](https://github.com/JohnSoi/link-shorter/actions/workflows/lint.yml/badge.svg)](https://github.com/JohnSoi/link-shorter/actions/workflows/lint.yml)