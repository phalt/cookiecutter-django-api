
install:
	pip install -r requirements.txt

build:
	python manage.py makemigrations resources
	python manage.py migrate
	python manage.py createsuperuser

serve:
	python manage.py runserver

drop_db:
	python manage.py flush

test:
	python manage.py test
