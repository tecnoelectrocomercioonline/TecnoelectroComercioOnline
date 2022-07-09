release: python manage.py makemigrations shop
release: python manage.py migrate shop
web: gunicorn ecom.wsgi --log-file - 
