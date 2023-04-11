from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.contrib.auth.models import User




# Create your models here.
ROLE_SELECTION = (
    ('U', 'User'),
    ('S', 'Service Provider'),
    
)

class UserRegistration(AbstractUser):
    role = models.CharField(max_length = 20, choices= ROLE_SELECTION , default = 'user')