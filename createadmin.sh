#rm db.sqlite3
#rm -rf ./areto/migrations
#rm -rf ./starwars/migrations
# PYTHONDONTWRITEBYTECODE=1 python manage.py dumpdata starwars --indent 2 > data/data.json
# PYTHONDONTWRITEBYTECODE=1 python manage.py loaddata data/data.json
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'python2020')" | PYTHONDONTWRITEBYTECODE=1 python manage.py shell

