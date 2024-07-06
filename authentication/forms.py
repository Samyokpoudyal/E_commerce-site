from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    phone=forms.CharField(max_length=10)

    class Meta:
        model= User
        fields=['username','email','phone','password1','password2']
