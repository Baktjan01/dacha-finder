#!/bin/bash

# Загружаем переменные окружения из .env
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

echo "Starting Django migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn server..."
exec gunicorn dacha_project.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3