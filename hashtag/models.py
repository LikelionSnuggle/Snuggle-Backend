from django.db import models
from django.conf import settings

# Create your models here.
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content


class Movie(models.Model):
    name = models.TextField(default=" ")
    hashtags = models.ManyToManyField(Hashtag, blank=True)