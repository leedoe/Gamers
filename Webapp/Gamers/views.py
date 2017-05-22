from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Q
from django.core.exceptions import ObjectDoesNotExist
from .models import Game, Developer, Publisher, Platform, Genre, Review
from .forms import GameForm, ReviewForm



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
    user = request.user
    game = Game.objects.get(pk=game_id)
    rating = Review.objects.filter(game = game_id).aggregate(Avg('score'))['score__avg']
    try:
        review_list = Review.objects.filter(Q(game=game_id), ~Q(user=user))
        my_review = Review.objects.get(game=game_id, user=user)
    except ObjectDoesNotExist:
        review_list = None
        my_review = None
    
    if rating == None:
        rating = 0

    context = {
        'game': game,
        'rating': rating,
        'review_list': review_list,
    }

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            if my_review is not None:
                review = Review(
                    user = user,
                    game = game,
                    score = form.cleaned_data['score'], 
                    content = form.cleaned_data['content'])
                review.save()
            else:
                my_review.score = form.cleaned_data['score']
                my_review.content = form.cleaned_data['content']
    else:
        if my_review is not None:
            form = ReviewForm(initial = {'score':my_review.score, 'content':my_review.content})
        else:
            form = ReviewForm()

    context['review_form'] = form

    return render(request, 'Gamers/content/game.html', context)


def game_list(request):
    game_list = Game.objects.all()

    gameandscore = []

    for item in game_list:
        rating = Review.objects.filter(game=item).aggregate(Avg('score'))['score__avg']
        if rating == None:
            rating = 0

        temp = {
            'game': item,
            'rating': rating,
        }
        
        gameandscore.append(temp)

    return render(request, 'Gamers/content/gamelist.html', {'gameandscore': gameandscore})
