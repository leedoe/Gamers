from django.shortcuts import render, redirect
from django.template.context import RequestContext
from .models import Game
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
    form = GameForm()

    data = None
    data = request.POST

    return render(request, 'Gamers/content/reg_game.html', {'form': form, 'data': data})
