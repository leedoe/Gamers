from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from .models import Game, Developer, Publisher, Platform, Genre
from .forms import GameForm


def login_page(request):
    user = request.user
    try:
        facebook_login = user.social_auth.get(provider='facebook')
        picture_url = 'http://graph.facebook.com/v2.8/' + facebook_login.uid + '/picture?type=square&hight=300&width=300&return_ssl_resources=1'
    except:
        facebook_login = None
        picture_url = None

    user = request.user

    if user == "AnonymousUser":
        return redirect("main")
    else:
        return render(request, 'Gamers/test.html')


def main(request):
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
        picture_url = 'http://graph.facebook.com/v2.8/' + facebook_login.uid + '/picture?type=small&return_ssl_resources=1'
    except:
        facebook_login = None
        picture_url = None

    return render(request, 'Gamers/main.html', {'game': Game.objects.all(), 'user': user, 'facebook_login': facebook_login, 'picture_url': picture_url})


def register_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)

        if form.is_valid():
            temp = form.save()

            return redirect('/game/' + str(temp.pk))
    else:
        form = GameForm()

    return render(request, 'Gamers/content/reg_game.html', {'form': form})


def game_viewer(request, game_id):
    game = Game.objects.get(pk=game_id)

    return render(request, 'Gamers/content/game.html', {'game': game})


def game_list(request):
    game_list = Game.objects.all()

    return render(request, 'Gamers/content/gamelist.html', {'game_list': game_list})
