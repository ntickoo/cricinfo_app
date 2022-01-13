from django.urls import path
from game import views

urlpatterns = [
    path(   "",     views.GamesAPIView.as_view(),   name="current_games"    ),
]