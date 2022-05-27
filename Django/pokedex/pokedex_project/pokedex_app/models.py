from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=100)
    image_back = models.CharField(max_length=100)
    types = models.CharField(max_length=100) 
    url = models.CharField(max_length=100)


    def __str__(self):
        return self.name + '' + self.number

class Deck(models.Model):
    user_assoc = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    poke_number = models.IntegerField(default= 0)
