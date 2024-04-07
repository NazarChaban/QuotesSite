from django.forms import (
    CharField, TextInput, PasswordInput, ModelForm, ImageField, FileInput
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    username = CharField(max_length=100, required=True, widget=TextInput())
    password1 = CharField(max_length=50, required=True, widget=PasswordInput())
    password2 = CharField(max_length=50, required=True, widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(ModelForm):
    avatar = ImageField(widget=FileInput())

    class Meta:
        model = Profile
        fields = ['avatar']
