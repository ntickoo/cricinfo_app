from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
import requests
from requests.exceptions import HTTPError
import json
from marshmallow import Schema, fields, post_load
from game.models import Game
from dotenv import load_dotenv
import os
load_dotenv()  # loads the configs from .env
class GameResultDto():
    def __init__(self, id, series_id, result, date, match_title):
        self.id             = id
        self.series_id      = series_id
        self.result         = result
        self.date           = date
        self.match_title    = match_title

    def __repr__(self):
        return '<game {}/{}>'.format(self.id, self.match_title)


class GameResultSchema(Schema):
    id              = fields.Int        (required = True)
    series_id       = fields.Int        (required = True)
    result          = fields.String     (required = True)
    date            = fields.DateTime   (required = True)
    match_title     = fields.String     (required = True)

    @post_load
    def make_game_result(self, data, **kwargs):
        return GameResultDto(**data)


@shared_task(name = "load_cricket_event_data_for_today")
def load_data():
    try:
        dtToday = datetime.today().strftime('%Y-%m-%d')
        print("Loading cricket event data for date - {}".format(dtToday))

        api_url = str(os.getenv('CRICKET_RESULT_URL'))

        url="{}/{}".format(api_url,dtToday)
        print(url)
        headers = {
            'x-rapidapi-host': str(os.getenv('API_HOST')),
            'x-rapidapi-key': str(os.getenv('API_KEY'))
            }

        response = requests.request("GET", url, headers=headers)
        response.raise_for_status()

        jsonResponse = response.json()

        # Deserailize to object and save.
        schema = GameResultSchema(unknown='EXCLUDE')
        game_results = schema.load(jsonResponse["results"], many=True)
        print(game_results)
        
        for gr in game_results:
            gameresult = Game( id = gr.id, seriesId = gr.series_id, result = gr.result, event_date = gr.date, title = gr.match_title)
            print("Going to save {}".format(gameresult))
            gameresult.save()
            print("Game {} inserted/updated successfully".format(gr))

    except requests.exceptions.HTTPError        as errh:
        print(errh)
    except requests.exceptions.ConnectionError  as errc:
        print(errc)
    except requests.exceptions.Timeout          as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)