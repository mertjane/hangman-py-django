# hangman_app/urls.py

from django.urls import path
from .views import start_game, play_game

urlpatterns = [
    path('start/', start_game, name='start_game'),
    path('play/<int:game_id>/', play_game, name='play_game'),
]
