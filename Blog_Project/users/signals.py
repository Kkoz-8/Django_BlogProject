from django.db.models.signals import post_save #the "post_save" signal is a signal that is fired/executed whenever an object is saved
from django.contrib.auth.models import User #The "User" model here will be the sender
from django.dispatch import receiver #obviously we need a receiver to receive signals from the sender
from .models import Profile #Our function will be creating a profile, as such we import the Profile model from the "modely.py" file in the "users" app


@receiver(post_save, sender = User) #Decorator "@receiver" with arguments for the signal "post_save" and the sender "User" #function "create_profile" modified to be a receiver
def create_profile(sender, instance, created, **kwargs): #"**kwargs" is here to grab any extra additional arguments
    #the "post_save" signal passes info to the parameters of "create_profile"
    if created:
        Profile.objects.create(user = instance) #variable "user" now represents an instance of the "User" that was created. please note upper and lower case "u" . they're not the same


@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()