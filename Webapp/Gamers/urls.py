"""reviewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^$', views.main, name='main'),
<<<<<<< HEAD
    url(r'^register/$', views.register_game, name='register_game'),
=======
    url(r'^register/$', views.RegisterGame.as_view(), name='register_game'),
>>>>>>> 2361a6267349eddd08c9a6f637abd9b10f8d9112
    url(r'^game/(?P<game_id>\d+)/$', views.game_viewer, name='game_viewer'),
    url(r'^gamelist/$', views.game_list, name='game_list'),
    url(r'^gamesearch/$', views.game_search, name='game_search'),
    url(r'^gamerc/$', views.game_recommendation_page,
        name="game_recommendation_page"),
    url(r'^rcgame/$', views.game_recommendation_cb,
        name="game_recommendation_cb"),
]