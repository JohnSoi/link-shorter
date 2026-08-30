#!/bin/bash
set -e

echo "🔄 Ожидание готовности PostgreSQL..."

# Ждём готовности PostgreSQL
while ! nc -z ${DATABASE_HOST} ${DATABASE_PORT}; do
    echo "PostgreSQL недоступен. Повторная попытка через 2 сек..."
    sleep 2
done

echo "✅ PostgreSQL доступен. Применяем миграции..."

# Применяем миграции
uv run alembic upgrade head

echo "✅ Миграции применены успешно."

# Запускаем основную команду
exec "$@"
