# Gamers/models.py

from django.db import models
from django.contrib.auth.models import User


# Game Developer
class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Game Publisher
class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Game Platform
class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Game Genre
class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Game Informations
class Game(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    homepage = models.URLField()
    developers = models.ManyToManyField(Developer)
    publishers = models.ManyToManyField(Publisher)
    platforms = models.ManyToManyField(Platform)
    genres = models.ManyToManyField(Genre)
    steam_id = models.IntegerField(null=True)

    def __str__(self):
        return self.title


# Game Picture
class Picture(models.Model):
    picture_url = models.URLField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture_url


# Game Review or scored
class Review(models.Model):
    user = models.ForeignKey(User)
    Game = models.ForeignKey(Game)
    score = models.IntegerField()
    content = models.TextField(null=True)
    write_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
