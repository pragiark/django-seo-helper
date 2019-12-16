from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=200)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name