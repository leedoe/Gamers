from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^modi_profile/$', views.modify_profile, name='modi'),
]