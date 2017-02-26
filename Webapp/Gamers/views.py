from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.


def test(request):
    user = request.user
    return render(request, 'Gamers/test.html', {'user': user})
