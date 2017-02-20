from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField()
    developer = models.CharField()
    publisher = models.CharField()
    release_date = models.DateTimeField()
    platform = models.CharField()
    genre = models.CharField()
    homepage = models.CharField()
    picture = models.CharField()

    def __str__(self):
        return self.title
