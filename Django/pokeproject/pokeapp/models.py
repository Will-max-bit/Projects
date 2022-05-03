from django.db import models

# Create your models here.
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
    