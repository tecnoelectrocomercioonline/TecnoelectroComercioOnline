# Delete Pycache
find . -name \*.pyc -delete

# Delete migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Delete sqllite3
rm -r db.sqlite3 
