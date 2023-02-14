from django import forms
from django.contrib.auth.models import User
from .models import * 

class CreateServiceForm(forms.Form):
    first_name = forms.CharField(max_length = 100, required=True)
    last_name = forms.CharField(max_length = 100, required=True)
    phone_number = forms.CharField(max_length = 100,required=True)
    salon_name = forms.CharField( max_length= 200, required=True)
    salon_services = forms.CharField(max_length= 200, required=True)
    opening_and_closing_time = forms.CharField(max_length= 200, required=True)
    location = forms.CharField(max_length= 200, required=True)
    image = forms.ImageField()
    salon_color = forms.CharField(max_length = 100)
    
    class Meta:
        model = CreateService
        fields = "__all__"