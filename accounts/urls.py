from django.urls import path
from .views import *


urlpatterns = [
    path('games/', get_games, name='games'),
    path('games/<int:pk>/', game_detail, name='game_detail'),

]
