from decimal import Decimal
from django.conf import settings
from accounts.models import Game
from django.db import models

class Cart(object):

    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем ПУСТУЮ корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебираем товары в корзине и получаем товары из базы данных.
        """
        game_ids = self.cart.keys()
        # получаем товары и добавляем их в корзину
        games = Game.objects.filter(id__in=game_ids)

        cart = self.cart.copy()
        for game in games:
            cart[str(game.id)]['game'] = game

        #for item in cart.values():
        for game_id, item in cart.items():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            item["game_id"] = game_id
            item["name"] = cart[game_id]['game'].name
            item["image"] = cart[game_id]['game'].image.url
            yield item
    
    def __len__(self):
        """
        Считаем сколько товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, game, quantity=1, update_quantity=False):
        """
        Добавляем товар в корзину или обновляем его количество.
        """
        game_id = str(game.id)
        if game_id not in self.cart:
            self.cart[game_id] = {'quantity': 0, 'price': str(game.price)}
        if update_quantity:
            self.cart[game_id]['quantity'] = quantity
        else:
            self.cart[game_id]['quantity'] += quantity
        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, game):
        """
        Удаляем товар
        """
        game_id = str(game.id)
        if game_id in self.cart:
            del self.cart[game_id]
            self.save()

    def get_total_price(self):
        # получаем общую стоимость
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # очищаем корзину в сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()
