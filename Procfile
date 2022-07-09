release: python manage.py migrate && python manage.py makemigrations
web: gunicorn ecom.wsgi --log-file - 
