from django import template
from accounts.views import Game
from django.core.serializers.json import DjangoJSONEncoder
import json

register = template.Library()


@register.simple_tag(name='get_games_names')
def get_percents_by_solution():
    games = Game.objects.all().values_list('id', 'name')
    return json.dumps(list(games), cls=DjangoJSONEncoder)
