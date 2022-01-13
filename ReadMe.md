# Set up
poetry install
set up redis on your machine
input your api key

# start web app
poetry run python manage.py runserver

# start celery for async task scheduler

## To send events
poetry run celery -A cricinfo_app beat -l info

## To see worker results
poetry run celery -A cricinfo_app  worker -l info 