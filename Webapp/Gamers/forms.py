from django import forms
from django.forms import ModelForm, CharField
from Gamers.widgets.widgets import TagsInputWidget, DatePickerWidget
from .models import Game, Developer, Publisher, Platform, Genre


class MyMultipleChoiceField(forms.ModelMultipleChoiceField):
    widget = TagsInputWidget

    def _check_values(self, value):
        return value[0].split(',')

"""
    def to_python(self, value):
        return [item for item in value]
"""

class GameForm(ModelForm):
    developers = MyMultipleChoiceField(queryset=Developer.objects.all())
    publishers = MyMultipleChoiceField(queryset=Publisher.objects.all())
    platforms = MyMultipleChoiceField(queryset=Platform.objects.all())
    genres = MyMultipleChoiceField(queryset=Genre.objects.all())

    class Meta:
        model = Game
        fields = ['title', 'release_date', 'homepage']
        widgets = {
            'release_date': DatePickerWidget,
        }

    def save(self, commit=True):
        data = self.cleaned_data
        print(data['developers'])
        title = self.cleaned_data['title']
        release_date = self.cleaned_data['release_date']
        homepage = self.cleaned_data['homepage']
        developers = self.cleaned_data['developers']
        publishers = self.cleaned_data['publishers']
        platforms = self.cleaned_data['platforms']
        genres = self.cleaned_data['genres']

        obj = Game(
            title=title,
            release_date=release_date,
            homepage=homepage,)
        obj.save()

        for item in developers:
            temp, created = Developer.objects.get_or_create(name=item)
            obj.developers.add(temp)

        for item in publishers:
            temp, created = Publisher.objects.get_or_create(name=item)
            obj.publishers.add(temp)

        for item in platforms:
            temp, created = Platform.objects.get_or_create(name=item)
            obj.platforms.add(temp)

        for item in genres:
            temp, created = Genre.objects.get_or_create(name=item)
            obj.genres.add(temp)