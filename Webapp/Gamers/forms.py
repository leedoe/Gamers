from django import forms
from django.forms import ModelForm, CharField
from Gamers.widgets.widgets import TagsInputWidget, DatePickerWidget, StarRatingWidget
from .models import Game, Developer, Publisher, Platform, Genre, Review


class MyMultipleChoiceField(forms.ModelMultipleChoiceField):
    widget = TagsInputWidget

    def _check_values(self, value):
        return value[0].split(',')


class GameForm(ModelForm):
    developers = MyMultipleChoiceField(queryset=Developer.objects.all())
    publishers = MyMultipleChoiceField(queryset=Publisher.objects.all())
    platforms = MyMultipleChoiceField(queryset=Platform.objects.all())
    genres = MyMultipleChoiceField(queryset=Genre.objects.all())

    class Meta:
        model = Game
        fields = ['title', 'release_date', 'homepage', 'developers', 'publishers', 'platforms', 'genres']
        widgets = {
            'release_date': DatePickerWidget,
        }

    def save(self, commit=True):
        #data = self.cleaned_data
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
            homepage=homepage,
            authen=0)
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

        return obj


    def __init__(self, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "게임명"
        self.fields['release_date'].label = "출시일"
        self.fields['homepage'].label = "홈페이지"
        #self.fields['developers'].label = "개발사 (태그는 ,(쉼표)로 구분해주세요.)"
        #self.fields['publishers'].label = "제공사 (태그는 ,(쉼표)로 구분해주세요.)"
        #self.fields['platforms'].label = "플랫폼 (태그는 ,(쉼표)로 구분해주세요.)"
        #self.fields['genres'].label = "장르 (태그는 ,(쉼표)로 구분해주세요.)"
        self.fields['homepage'].widget.attrs['placeholder'] = "ex) http://test.com"
        #self.fields['developers'].widget.attrs['class'] = 'browser-default'


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['score', 'content']
        widgets = {
            'score': StarRatingWidget
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = False