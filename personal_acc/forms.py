from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username',)

class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ('username',)