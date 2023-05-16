from django.shortcuts import render
from .models import Game


def get_games(request):
    context = {}
    context['games'] = Game.objects.all()
    return render(request, 'games.html', context)
