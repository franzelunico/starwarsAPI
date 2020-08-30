python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 

python manage.py makemigrations
python manage.py createsuperuser --username admin --email admin@gmail.com

python manage.py makemigrations starwars
python manage.py migrate starwars


