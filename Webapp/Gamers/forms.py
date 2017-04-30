from django.forms import ModelForm
from Gamers.widgets.tagsinput import TagsInputWidget
from .models import Game

class GameForm(ModelForm):
	class Meta:
		model = Game
		fields = ['title', 'release_date', 'homepage', 'developers', 'publishers', 'platforms', 'genres']
		widgets = {
			'developers': TagsInputWidget,
			'publishers': TagsInputWidget,
			'platforms': TagsInputWidget,
			'genres': TagsInputWidget,
		}