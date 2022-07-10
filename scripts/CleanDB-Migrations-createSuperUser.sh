# Delete Pycache
find . -name \*.pyc -delete

# Delete migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Delete sqllite3
rm -r db.sqlite3 

# Makemigrations && migrate
python3 manage.py makemigrations authentication
python3 manage.py makemigrations shop
python3 manage.py migrate

#Crete Super User
python3 manage.py createsuperuser --username=nigarumovum --email=bfpr131095@gmail.com
