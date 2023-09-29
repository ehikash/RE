from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Profile, DieselRequests #since we are creating Profile for every new user
#created a signal where User act as the sender since we want to automatically create a Profile for every User created 


@receiver(post_save, sender=User) #when a user is saved, send a signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) #everytime a user is created, we create a profile
        
@receiver(post_save, sender=User) #when a user is saved, send a signal
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
        
# @receiver(post_save, sender=DieselRequests) #when a request is saved, send a signal
# def create_request(sender, instance, created, **kwargs):
#     if created:
#         DieselRequests.objects.create(manager=instance)
        

# @receiver(post_save, sender=DieselRequests) #when a user is saved, send a signal
# def save_request(sender, instance, **kwargs):
#     instance.request.save()