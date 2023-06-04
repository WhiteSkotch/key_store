from django.shortcuts import render, get_object_or_404
from .models import Game


def get_games(request):
    context = {}
    context['games'] = Game.objects.all()
    return render(request, 'games.html', context)


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return  render(request, 'game_detail.html', {'game':game})


def aboutstore(request):
    return render(request, 'aboutstore.html')


def agreement(request):
    return render(request, 'agreement.html')


def guarantees(request):
    return render(request, 'guarantees.html')


def refund(request):
    return render(request, 'refund.html')


def support(request):
    return render(request, 'support.html')