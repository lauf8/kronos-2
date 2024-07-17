#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Esperando pelo PostgreSQL..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL iniciado"
fi

# Aplicar migrações do Django
python manage.py migrate

# Coletar arquivos estáticos do Django
python manage.py collectstatic --noinput

exec "$@"
