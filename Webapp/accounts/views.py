from django.shortcuts import render, redirect
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Avg
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import UsernameEditForm
from Gamers.models import Review


def login(request):
    providers = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(
        request,
        #authentication_form=LoginForm, 
        template_name='accounts/login_form.html', 
        extra_context={'providers': providers}
    )


@login_required
def profile(request):
    myreviewlist = []
    myreview = Review.objects.filter(user=request.user)
    for review in myreview:
        gamescore = Review.objects.filter(game=review.game).aggregate(Avg('score'))['score__avg']
        myreviewlist.append({'myreview': review, 'gamescore':gamescore})


    return render(request, 'accounts/profile.html', {'myreviewlist': myreviewlist})


@login_required
def modify_profile(request):
    user = request.user
    originalname = request.user.username
    if request.method == 'POST':
        form = UsernameEditForm(request.POST, instance=user)

        if form.is_valid():
            form.save()

            return redirect("profile")
        else:
            user.username = originalname
    else:
        form = UsernameEditForm(initial = {'username': user.username})

    return render(request, 'accounts/modi_profile.html', {'form': form})