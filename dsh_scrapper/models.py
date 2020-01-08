from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=200)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class PageStatus(models.Model):
    body = models.TextField()
    status = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)