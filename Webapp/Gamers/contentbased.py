import os
import django
import json
import heapq
import queue
import timeit

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "reviewer.settings")
django.setup()

from Gamers.models import Game, Developer, Genre, Publisher, Platform, \
    Screenshot, Tag


def contentbasedfiltering(targettitle):
    with open('./gamelist.json', 'r') as f:
            gamelist = json.load(f)

    target = gamelist[targettitle]
    rawgamelist = [(0, 0), (0, 0), (0, 0)]
    recommendedgame = []

    for game in gamelist.values():
        count = 0

        if target['title'] == game['title']:
            continue

        for developer in target['developers']:
            if developer in game['developers']:
                count += 0.3

        for genre in target['genres']:
            if genre in game['genres']:
                count += 0.5

        for tag in target['tags']:
            if tag in game['tags']:
                count += 0.7

        if rawgamelist[0][0] <= count:
            rawgamelist[1:3] = rawgamelist[0:2]
            rawgamelist[0] = (count, game['title'])

    for count, game in rawgamelist:
        gameobject = Game.objects.get(title=game)
        screenshot = Screenshot.objects.filter(game=gameobject)[0]

        recommendedgame.append((gameobject, screenshot))

    return recommendedgame
