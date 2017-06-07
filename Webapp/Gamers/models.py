# Gamers/models.py

from django import forms
from django.db import models
from django.contrib.auth.models import User


# Game Developer
class Developer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Game Publisher
class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Game Platform
class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Game Genre
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Game Informations
class Game(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,)
    release_date = models.DateField()
    homepage = models.URLField(null=True)
    developers = models.ManyToManyField(Developer)
    publishers = models.ManyToManyField(Publisher)
    platforms = models.ManyToManyField(Platform)
    genres = models.ManyToManyField(Genre)
    authen = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Game Screenshot
class Screenshot(models.Model):
    screenshot_url = models.URLField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.game.title


# Game Review or scored
class Review(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    score = models.IntegerField()
    content = models.TextField(null=True)
    write_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'game')
