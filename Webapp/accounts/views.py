from django.shortcuts import render
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import UsernameEditForm


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
    user = request.user
    if request.method == 'POST':
        form = UsernameEditForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
    else:
        form = UsernameEditForm(initial={'username': user.username,'email': user.email})

    return render(request, 'accounts/profile.html', {'form': form})