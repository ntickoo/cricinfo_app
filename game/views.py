from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from game.serializers import GameSerializer
from game.models import Game
from datetime import datetime, timedelta
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from rest_framework.exceptions import ValidationError

# Create your views here.
@api_view(['GET'])
def game_results_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        games               = Game.objects.all()
        event_date          = request.query_params.get('event-date', None)
        if event_date is not None:
            validate_event_date(event_date)
            event_start_date    = datetime.strptime(event_date, '%Y-%m-%d')
            event_end_date      = event_start_date + timedelta(days=1)
            games               = games.filter(event_date__gte=event_start_date, event_date__lt=event_end_date)
        game_serializer     = GameSerializer(games, many=True)
        return JsonResponse(game_serializer.data, safe=False)


def validate(date_text):
    try:
        datetime.strptime(str(date_text), '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_event_date(date):
    if not validate(date):
        raise ValidationError(detail="date is not in valid format YYYY-MM-DD")