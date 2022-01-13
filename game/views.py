from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from game.serializers import GameSerializer
from game.models import Game

# Create your views here.
@api_view(['GET'])
def game_results_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        games = Game.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            games = games.filter(title__icontains=title)
        
        game_serializer = GameSerializer(games, many=True)
        return JsonResponse(game_serializer.data, safe=False)