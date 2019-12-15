from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
