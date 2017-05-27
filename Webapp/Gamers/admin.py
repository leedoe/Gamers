# Gamers/admin.py
from django.contrib import admin
from .models import Developer, Genre, Platform, Publisher, Screenshot, Game, Review

admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Platform)
admin.site.register(Developer)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Screenshot)
