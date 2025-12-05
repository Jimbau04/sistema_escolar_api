pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn dev_sistema_escolar_api.wsgi:application --bind
