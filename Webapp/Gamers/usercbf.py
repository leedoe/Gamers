import os
import json
from operator import itemgetter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', ".reviewer.settings")
import django
django.setup()
from Gamers.models import Game, Genre, Tag, Review, Developer, Screenshot
from django.contrib.auth.models import User
from django.db.models import Avg


def usercbf(username):
    with open('./gamelist.json', 'r') as f:
            gamelist = json.load(f)

    dojun = User.objects.get(username="도준이")

    reviews = Review.objects.filter(user=dojun)
    reviewedgamelist = [x.game.title for x in reviews]

    utdict = {}
    ugdict = {}
    uddict = {}

    for review in reviews:
        game = Game.objects.get(title=review.game)

        tags = game.tags.all()
        genres = game.genres.all()
        developers = game.developers.all()

        for tag in tags:
            if tag.name in utdict:
                utdict[tag.name] += 0.1 * review.score
            else:
                utdict[tag.name] = 0.1 * review.score

        for genre in genres:
            if genre.name in ugdict:
                ugdict[genre.name] += 0.1 * review.score
            else:
                ugdict[genre.name] = 0.1 * review.score

        for developer in developers:
            if developer in uddict:
                uddict[developer.name] += 0.1 * review.score
            else:
                uddict[developer.name] = 0.1 * review.score

    rawgamelist = []

    for game in gamelist.values():
        count = 0

        if game['title'] in reviewedgamelist:
            continue

        for developer, score in uddict.items():
            if developer in game['developers']:
                count += 0.3 * score

        for genre, score in ugdict.items():
            if genre in game['genres']:
                count += 0.5 * score

        for tag, score in utdict.items():
            if tag in game['tags']:
                count += 0.7 * score

        rawgamelist.append({'title': game['title'], 'score': count})

    temp = sorted(rawgamelist, key=itemgetter('score'), reverse=True)

    recommendedgames = temp[:9]
    recogame = [[], [], []]
    for i, rgame in enumerate(recommendedgames):
        go = Game.objects.get(title=rgame['title'])
        sc = Screenshot.objects.filter(game=go)[0]
        score = Review.objects.filter(game=go).aggregate(Avg('score'))['score__avg']

        recogame[int(i / 3)].append({
            'game': go,
            'screenshot': sc,
            'score': score,
        })

    return recogame
