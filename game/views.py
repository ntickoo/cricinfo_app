from django.shortcuts import render
from rest_framework.generics import ListAPIView
from game.serializers import GameSerializer
from game.models import Game

# Create your views here.


# Create your views here.
class GamesAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer