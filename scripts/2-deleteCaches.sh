# Delete Caches
find . -name \*.pyc -delete

python3 manage.py collectstatic
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate shop
python3 manage.py makemigrations shop
python3 manage.py migrate auth
python3 manage.py makemigrations auth
python3 manage.py migrate
python3 manage.py makemigrations