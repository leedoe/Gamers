from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length = 100)
    developer = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 100)
    release_date = models.DateTimeField()
    platform = models.CharField(max_length = 30)
    genre = models.CharField(max_length = 100)
    homepage = models.CharField(max_length = 100)
    picture = models.CharField(max_length = 100)

    def __str__(self):
        return self.title


class Gamer(User):
    def __str__(self):
        return self.username