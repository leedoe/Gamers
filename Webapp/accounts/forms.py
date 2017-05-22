# accounts/forms.py
from django import forms
from django.contrib.auth.models import User


class UsernameEditForm(forms.ModelForm):
    """
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UsernameEditForm, self).__init__(*args, **kwargs)
        print(user.username)
        self.fields['username'].value = user.username
        self.fields['email'].value = user.email
    """

    class Meta:
        model = User
        fields = ['username', 'email']