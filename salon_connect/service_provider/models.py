from django.db import models

from django.db.models.signals import pre_save

# Create your models here.
class CreateService(models.Model):
    first_name = models.CharField(max_length= 200, unique=True)
    last_name = models.CharField(max_length= 200, unique=True)
    phone_number = models.CharField(max_length= 200, unique=True)
    salon_name = models.CharField(max_length= 200, unique=False)
    salon_services = models.TextField(max_length= 200, unique=False)
    opening_and_closing_time = models.CharField(max_length= 200, unique=False)
    location =models.CharField(max_length= 200, unique=False)
    image = models.ImageField(upload_to= 'img/service_provider', height_field=None, width_field=None, max_length=None, unique=False)
    salon_color = models.CharField(max_length= 200, null = False, unique=False)
