sleep 4
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
exec "$@"