# Gamers/models.py

from django.db import models
from django.contrib.auth.models import User


# Game Developer
class Developer(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE,
    )
    developer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.developer_name


# Game Publisher
class Publisher(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE
    )
    publisher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.publisher_name


# Game Platform
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
        on_delete=models.CASCADE
    )
    publisher_name = models.CharField(
        max_length=20,
        choices=PLATFORM_LIST_CHOICES,
    )

    def __str__(self):
        return self.publisher_name


# Game Genre
class Genre(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE
    )
    genre_name = models.CharField(max_length=20)


# Game Picture
class Picture(models.Model):
    game = models.ForeignKey(
        'Game',
        on_delete=models.CASCADE
    )
    picture_url = models.URLField()


# Game Informations
class Game(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    homepage = models.URLField()
    steam_id = models.IntegerField(null=True)

    def __str__(self):
        return self.title


# Game Review or scored
class Review(models.Model):
    user = models.ForeignKey(User)
    Game = models.ForeignKey(Game)
    score = models.IntegerField()
    content = models.TextField(null=True)
    write_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)