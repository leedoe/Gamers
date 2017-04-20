from django.forms import ModelForm
from .models import Game

class GameForm(ModelForm):
	class Meta:
		model = Game
		fields = ['title', 'release_date', 'homepage', 'developers', 'publishers', 'platforms', 'genres']