from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    system_requirements = models.TextField()
    image = models.ImageField(upload_to='static/img')
    discount = models.DecimalField(max_digits=3, decimal_places=0, default=5)


class Key(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    key = models.CharField(max_length=50, unique=True)
    is_sold = models.BooleanField(default=False)


class Money(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balance')
    money = models.DecimalField(max_digits=15, decimal_places=2, default=0)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
