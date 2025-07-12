from django import forms
from .models import Idea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'image']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
