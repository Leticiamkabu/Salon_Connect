from django.db import models

from django.db.models.signals import pre_save

# Create your models here.
class CreateService(models.Model):
    first_name = models.CharField(max_length= 200, unique=True)
    last_name = models.CharField(max_length= 200, unique=True)
    phone_number = models.CharField(max_length= 200, unique=True)
    salon_name = models.CharField(max_length= 200, unique=True)
    salon_services = models.TextField(max_length= 200, unique=True)
    opening_and_closing_time = models.CharField(max_length= 200, unique=True)
    location =models.CharField(max_length= 200, unique=True)
    image = models.ImageField(upload_to= 'service_provider/', height_field=None, width_field=None, max_length=None, default = True , unique=True)
    salon_color = models.CharField(max_length= 200, null = False, unique=True)
