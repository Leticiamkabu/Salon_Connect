from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.db.models.signals import pre_save
from authentication.models import UserRegistration

# Create your models here.

# class Users(AbstractUser):
    
    
class CreateService(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, related_name='services', null = True, blank=True)
    first_name = models.CharField(max_length= 200, unique=True)
    last_name = models.CharField(max_length= 200, unique=True)
    phone_number = models.CharField(max_length= 200, unique=True, default = "0000000000")
    salon_name = models.CharField(max_length= 200, unique=False, default = "None")
    salon_services = models.TextField(max_length= 200, unique=False, default = "None")
    opening_and_closing_time = models.CharField(max_length= 200, unique=False, default = "00:00")
    location =models.CharField(max_length= 200, unique=False, default = "None")
    image = models.ImageField(upload_to= 'img/service_provider', unique=False, default = "None")
    salon_color = models.CharField(max_length= 200, null = False, unique=False , default = "None")
