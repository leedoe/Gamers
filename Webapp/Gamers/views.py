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
        print(request.POST)

        if form.is_valid():
            """
            data = request.POST

            title = form.cleaned_data['title']
            release_date = form.cleaned_data['release_date']
            homepage = form.cleaned_data['homepage']
            developers = data.get('developers').split(',')
            publishers = data.get('publishers').split(',')
            platforms = data.get('platforms').split(',')
            genres = data.get('genres').split(',')

            obj = Game(
                title=title,
                release_date=release_date,
                homepage=homepage,)
            obj.save()

            for item in developers:
                temp, created = Developer.objects.get_or_create(name=item)
                obj.developers.add(temp)

            for item in publishers:
                temp, created = Publisher.objects.get_or_create(name=item)
                obj.publishers.add(temp)

            for item in platforms:
                temp, created = Platform.objects.get_or_create(name=item)
                obj.platforms.add(temp)

            for item in genres:
                temp, created = Genre.objects.get_or_create(name=item)
                obj.genres.add(temp)
            """
            form.save()
    else:
        form = GameForm()

    return render(request, 'Gamers/content/reg_game.html', {'form': form})
