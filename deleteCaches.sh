find . -name \*.pyc -delete

python3 manage.py migrate
python3 manage.py makemigrations