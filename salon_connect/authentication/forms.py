# for authentication
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class RegisterationForm(forms.ModelForm):
    username = forms.CharField(max_length = 100, required=True)
    password1 = forms.CharField(max_length=100, label = 'Password', widget = forms.PasswordInput())
    password2 = forms.CharField(max_length = 100,label = 'Confirm Password', required=True, widget = forms.PasswordInput())
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices= ROLE_SELECTION, required = True)
    
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "role",)
        
    