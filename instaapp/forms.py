from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=40)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'caption')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']