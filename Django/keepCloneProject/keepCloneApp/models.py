from django.db import models
from django.utils import timezone
# Create your models here.
class Save_Note(models.Model):
    title = models.TextField(max_length=100)
    note = models.CharField(max_length=1000000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title