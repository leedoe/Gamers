import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "reviewer.settings")

import django
django.setup()
from Gamers.models import Game, Developer, Genre, Publisher, Platform, \
    Screenshot, Tag

with open('./gamelist.json', 'r') as f:
        gamesinjson = json.load(f)

gamesindb = Game.objects.all()

for gameindb in gamesindb:
    if gameindb.title not in gamesinjson:
        content = {}
        content['title'] = gameindb.title
        content['release_date'] = str(gameindb.release_date)
        content['homepage'] = gameindb.homepage
        content['platforms'] = [x.name for x in gameindb.platforms.all()]
        content['genres'] = [x.name for x in gameindb.genres.all()]
        content['developers'] = [x.name for x in gameindb.developers.all()]
        content['publishers'] = [x.name for x in gameindb.publishers.all()]
        content['screenshot'] = Screenshot.objects.get(game=gameindb)\
            .screenshot_url
        content['tags'] = [x.name for x in gameindb.tags.all()]

        # gamesinjson[gameindb.title] = content
"""
with open("./gamelist.json", 'w') as f:
    json.dump(gamesinjson, f)
"""
# print(gamesinjson)