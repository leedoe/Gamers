from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Q
from django.contrib.auth.decorators import login_required
from .models import Game, Developer, Publisher, Platform, Genre, Review, Screenshot, Tag
from .forms import GameForm, ReviewForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json



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
    return render(request, 'Gamers/main.html')


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
    game = Game.objects.get(pk=game_id)
    rating = Review.objects.filter(game = game_id).aggregate(Avg('score'))['score__avg']
    screenshot = Screenshot.objects.get(game=game_id).screenshot_url

    if request.user.is_authenticated == True:
        user = request.user
        try:
            review_list = Review.objects.filter(Q(game=game_id), ~Q(user=user))
        except ObjectDoesNotExist:
            review_list = None

        try:
            my_review = Review.objects.get(game=game_id, user=user)
        except ObjectDoesNotExist:
            my_review = None
    else:
        try:
            review_list = Review.objects.filter(game=game_id)
        except ObjectDoesNotExist:
            review_list = None
        
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
    gameandscore = []
    game_list = Game.objects.filter(authen=True).order_by('-release_date')
    paginator = Paginator(game_list, 15)

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    for item in contacts.object_list:
        rating = Review.objects.filter(game=item).aggregate(Avg('score'))['score__avg']
        if rating == None:
            rating = 0

        screenshot = Screenshot.objects.get(game=item).screenshot_url

        temp = {
            'game': item,
            'rating': rating,
            'screenshot': screenshot
        }
        
        gameandscore.append(temp)

    gameandscore = [gameandscore[i:i+3] for i in range(0, len(gameandscore), 3)]

    
    if int(page) % 5 == 0:
        page_start = int(int(page) / 5 - 1) * 5 + 1
    else:
        page_start = int(int(page) / 5) * 5 + 1
    page_end = page_start + 5
    if page_end > paginator.num_pages:
            page_end = paginator.num_pages + 1
    return render(request, 'Gamers/gamelist.html', {'gameandscore': gameandscore, 'pagination': contacts, 'range': range(page_start, page_end)})
"""
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
"""


def game_search(request):
    contacts = None
    gameandscore = []
    searched_list = None

    gametitle = {}
    developername = {}
    publishername = {}
    genrename = {}
    tagname = {}
    for item in Game.objects.all().order_by('title'):
        gametitle[item.title] = None

    for item in Developer.objects.all().order_by('name'):
        developername[item.name] = None

    for item in Publisher.objects.all().order_by('name'):
        publishername[item.name] = None

    for item in Genre.objects.all().order_by('name'):
        genrename[item.name] = None
    
    for item in Tag.objects.all().order_by('name'):
        tagname[item.name] = None

    autocomplete_data = {
        'gametitle': json.dumps(gametitle),
        'developername': json.dumps(developername),
        'publishername': json.dumps(publishername),
        'genrename': json.dumps(genrename),
        'tagname': json.dumps(tagname),
    }

    if request.GET.get('section') != None:
        inputitem = {
            'section': request.GET.get('section'),
            'item': request.GET.get('item'),
        }

        if inputitem['section'] == 'gam_name':
            searched_list = Game.objects.filter(title__icontains=inputitem['item']).order_by('-release_date')
        elif inputitem['section'] == 'dev_name':
            searched_list = Game.objects.filter(developers__name__icontains=inputitem['item']).order_by('-release_date')
        elif inputitem['section'] == 'pub_name':
            searched_list = Game.objects.filter(publishers__name__icontains=inputitem['item']).order_by('-release_date')
        elif inputitem['section'] == 'gen_name':
            searched_list = Game.objects.filter(genres__name__icontains=inputitem['item']).order_by('-release_date')
        elif inputitem['section'] == 'tag_name':
            searched_list = Game.objects.filter(tags__name__icontains=inputitem['item']).order_by('-release_date')

        paginator = Paginator(searched_list, 15)

        page = request.GET.get('page')

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        for game in contacts.object_list:
            rating = Review.objects.filter(game=game).aggregate(Avg('score'))['score__avg']
            if rating == None:
                rating = 0

            screenshot = Screenshot.objects.get(game=game).screenshot_url

            temp = {
                'game': game,
                'rating': rating,
                'screenshot': screenshot
            }
            
            gameandscore.append(temp)

        gameandscore = [gameandscore[i:i+3] for i in range(0, len(gameandscore), 3)]

        
        if int(page) % 5 == 0:
            page_start = int(int(page) / 5 - 1) * 5 + 1
        else:
            page_start = int(int(page) / 5) * 5 + 1
        page_end = page_start + 5
        if page_end > paginator.num_pages:
            page_end = paginator.num_pages + 1

        return render(request, 'Gamers/game_search.html', {'isContent': True, 'gameandscore': gameandscore, 'pagination': contacts, 'range': range(page_start, page_end), 'inputitem': inputitem, 'autocomplete_data': autocomplete_data})
    return render(request, 'Gamers/game_search.html', {'isContent': False, 'autocomplete_data': autocomplete_data})
    