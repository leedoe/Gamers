# Gamers/admin.py
from django.contrib import admin
from .models import Developer, Genre, Platform, Publisher, Screenshot, Game, Review, Tag, ThumbUpDown

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'get_platforms')

    def get_platforms(self, obj):
        return ",".join([p.name for p in obj.platforms.all()])

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    search_fields = ['name',]


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    search_fields = ['name',]

admin.site.register(Game, GameAdmin)
admin.site.register(Review)
admin.site.register(Platform)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Genre)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Tag)
admin.site.register(Screenshot)
admin.site.register(ThumbUpDown)