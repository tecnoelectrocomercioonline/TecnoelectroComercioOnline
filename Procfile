release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn ecom.wsgi --log-file - 
