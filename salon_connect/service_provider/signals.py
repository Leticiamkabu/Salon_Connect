from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CreateService

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        CreateService.objects.create(user=instance)
  
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()

