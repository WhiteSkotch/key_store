from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Key(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    key = models.CharField(max_length=50, unique=True)


class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
