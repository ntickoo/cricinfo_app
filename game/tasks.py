from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
import requests
from requests.exceptions import HTTPError
import json

@shared_task(name = "print_msg_with_name")
def print_message(name, *args, **kwargs):
  print("Celery is working!! {} have implemented it correctly.".format(name))

@shared_task(name = "add_2_numbers")
def add(x, y):
  print("Add function has been called!! with params {}, {}".format(x, y))
  return x+y



@shared_task(name = "load_cricket_event_data_for_today")
def load_data():
  try:
    dtToday = datetime.today().strftime('%Y-%m-%d')
    print("Loading cricket event data for date - {}".format(dtToday))

    url = "http://localhost:3010/game-results"

    headers = {
        'x-rapidapi-host': "cricket-live-data.p.rapidapi.com",
        'x-rapidapi-key': "1556516c5bmsh4d080d73a653a23p1b3381jsn483c667958c8"
        }

    response = requests.request("GET", url, headers=headers)
    jsonResponse = response.json()
    print(jsonResponse["results"])
    item_dict = json.loads(response.text)
    print(len(item_dict['results']))

  except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
  except Exception as err:
    print(f'Other error occurred: {err}')