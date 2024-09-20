
sleep 10

python manage.py migrate
# Coletar arquivos estáticos
python manage.py collectstatic --noinput

exec "$@"

