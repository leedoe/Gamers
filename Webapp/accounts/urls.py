from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from allauth.account.views import LoginView
from . import views

urlpatterns = [
    # url(r'^login/$', auth_views.login, name='login',
    #    kwargs={'template_name': 'accounts/login_form.html'}),
    url(r'^login/$', views.login, name='login'),
    #url(r'^login/$', LoginView, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^social/signup/$', views.signup, name='socialaccount_signup'),
]