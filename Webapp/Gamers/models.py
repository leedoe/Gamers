from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Developer(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete = models.CASCADE,
        )
    developer_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.developer_name


class Publisher(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete = models.CASCADE
        )
    publisher_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.publisher_name


class Platform(models.Model):
    PLATFORM_LIST_CHOICES = (
        ('WINDOWS', 'Windows'),
        ('MAC', 'Mac'),
        ('LINUX', 'LINUX'),
        ('PS4', 'PLAYSTATION 4'),
        ('XBOX ONE', 'XBOX ONE'),
        ('PS3', 'PLAYSTATION 3'),
        ('XBOX 360', 'XBOX 360')

    )
    game = models.ForeignKey(
        'Game',
        on_delete = models.CASCADE
        )
    publisher_name = models.CharField(
        max_length = 20,
        choices = PLATFORM_LIST_CHOICES,
        )

    def __str__(self):
        return self.publisher_name


class Genre(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete = models.CASCADE
        )
    genre_name = models.CharField(max_length = 20)


class Pictures(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete = models.CASCADE
        )
    picture_url = models.URLField()


class Game(models.Model):
    name = models.CharField(max_length = 100)
    release_date = models.DateTimeField()
    homepage = models.URLField()

    def __str__(self):
        return self.title


class Gamer(User):
    def __str__(self):
        return self.username