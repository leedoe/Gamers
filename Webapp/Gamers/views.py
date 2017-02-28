from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.


def test(request):
    user = request.user

    facebook_login = user.social_auth.get(provider='facebook')
    picture_url = 'http://graph.facebook.com/v2.8/' + facebook_login.uid + '/picture?type=square&hight=600&width=600&return_ssl_resources=1'

    return render(request, 'Gamers/test.html', {'facebook_login': facebook_login, "picture_url": picture_url})
