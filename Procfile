release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
python manage.py collectstatic --noinput

web: gunicorn AASYSTEM.wsgi