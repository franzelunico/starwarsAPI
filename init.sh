rm db.sqlite3
rm -rf ./areto/migrations
rm -rf ./starwars/migrations

PYTHONDONTWRITEBYTECODE=1 python manage.py migrate
PYTHONDONTWRITEBYTECODE=1 python manage.py makemigrations starwars
PYTHONDONTWRITEBYTECODE=1 python manage.py migrate starwars
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'python2020')" | PYTHONDONTWRITEBYTECODE=1 python manage.py shell
# python manage.py dumpdata starwars --indent 2 > data/data.json
# PYTHONDONTWRITEBYTECODE=1 python manage.py loaddata data/data.json
PYTHONDONTWRITEBYTECODE=1 python manage.py runserver 0.0.0.0:8081


# from starwars.models import Personaje, Rating
# luke = Personaje.objects.get(pk=1)
# votos_luke = Rating.objects.filter(personaje=luke)
# from django.db.models import Avg
# votos_luke.aggregate(Avg('rating'))