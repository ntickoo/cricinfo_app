# Set up
1. poetry install
2. set up redis on your machine (used as  message broker for celery)
3. input your api key

# start web app
poetry run python manage.py runserver

# start celery for async task scheduler

## To send events
poetry run celery -A cricinfo_app beat -l info

## To see worker results
poetry run celery -A cricinfo_app  worker -l info 