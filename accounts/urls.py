from django.urls import path
from .views import *


urlpatterns = [
    path('games/', get_games, name='games'),
]
