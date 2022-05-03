from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    image = forms.ImageField(required=False)

    class Meta:
        #this is a comment for testing
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'image']