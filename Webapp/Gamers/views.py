from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.


def test(request):
	user = request.user
	
	try:
		facebook_login = user.social_auth.get(provider='facebook')
	except:
		facebook_login = None

	return render(request, 'Gamers/test.html', {'facebook_login': facebook_login,})
