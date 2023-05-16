from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=128)

class Key(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    key = models.CharField(max_length=50, unique=True)

class User(models.Model):
    login = models.CharField(unique=True, max_length=30)
    password = models.CharField(unique=True,max_length=50)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
