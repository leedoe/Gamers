from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Q
from django.contrib.auth.decorators import login_required
from .models import Game, Developer, Publisher, Platform, Genre, Review, Screenshot
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


    game_list = []
    temp = []
    i = 0
    for item in Game.objects.all():
        try:
            sc = Screenshot.objects.get(game=item)
        except:
            sc = None
        tu = (item, sc)
        temp.append(tu)
        i = i + 1
        if i == 4:
            game_list.append(temp)
            temp = []
            i = 0

    return render(request, 'Gamers/main.html', {'game': game_list, 'page_title': 'TESTPAGE'})


def register_game(request):
    if request.method == 'POST':
        #print(request.POST)
        form = GameForm(request.POST)

        if form.is_valid():
            form.authen = False
            temp = form.save()

            return redirect('/game/' + str(temp.pk))
    else:
        form = GameForm()

    return render(request, 'Gamers/reg_game.html', {'form': form, 'page_title': 'REGISTER'})


def game_viewer(request, game_id):
    user = request.user
    game = Game.objects.get(pk=game_id)
    rating = Review.objects.filter(game = game_id).aggregate(Avg('score'))['score__avg']
    screenshot = Screenshot.objects.get(game=game_id).screenshot_url

    try:
        review_list = Review.objects.filter(Q(game=game_id), ~Q(user=user))
    except ObjectDoesNotExist:
        review_list = None

    try:
        my_review = Review.objects.get(game=game_id, user=user)
    except ObjectDoesNotExist:
        my_review = None
    
    if rating == None:
        rating = 0

    context = {
        'game': game,
        'rating': rating,
        'review_list': review_list,
        'screenshot': screenshot,
    }

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            if my_review is None:
                review = Review(
                    user = user,
                    game = game,
                    score = form.cleaned_data['score'], 
                    content = form.cleaned_data['content'])
                print(form.cleaned_data['content'])
                review.save()
            else:
                my_review.score = form.cleaned_data['score']
                my_review.content = form.cleaned_data['content']
                my_review.save()
    else:
        if my_review is None:
            form = ReviewForm()
        else:
            form = ReviewForm(initial = {'score':my_review.score, 'content':my_review.content})

    context['review_form'] = form

    return render(request, 'Gamers/game_viewer.html', context)


def game_list(request):
    game_list = Game.objects.filter(authen=True)

    gameandscore = []

    for item in game_list:
        rating = Review.objects.filter(game=item).aggregate(Avg('score'))['score__avg']
        if rating == None:
            rating = 0

        try:
            screenshot = Screenshot.objects.get(game=item).screenshot_url
        except:
            screenshot = None

        temp = {
            'game': item,
            'rating': rating,
            'screenshot': screenshot
        }
        
        gameandscore.append(temp)

    gameandscore = [gameandscore[i:i+3] for i in range(0, len(gameandscore), 3)]

    return render(request, 'Gamers/gamelist.html', {'gameandscore': gameandscore})
