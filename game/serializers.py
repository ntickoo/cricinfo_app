from rest_framework import serializers
from game.models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class EventDatesSerializer(serializers.Serializer[any]):
    event_date = serializers.DateField(required=False, format='%Y-%m-%d')