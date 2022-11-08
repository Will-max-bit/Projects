from django.db import models
from django.utils import timezone
# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    note_body = models.TextField(max_length=5000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title