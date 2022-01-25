from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model): #our class "Profile" inheriting from models.Model
    #Remember CASCADE is one way, in this case, if user is deleted, their profile is deleted, but if profile is deleted, user is not.
    user = models.OneToOneField(User, on_delete = models.CASCADE) #1 to 1 relationship, one user can have 1 profile and 1 profile will be associated with one user
    image = models.ImageField(default = "rip.png", upload_to = "profile_images")
    #HOW I THINK IT WORKS:
        #So when a user is created, the "user" variable here will basically be a exact replication of the values for the created user, e.g, email, username etc
        #So the profile created has access to all fields in the "User" model
        #The "image" variable represents a new field that is added to the Profile of the user

    def __str__(self):
        return f"Profile for user: {self.user.username}"

    #To resize images we need to over-ride the save method of our Profile model
    #Add in *args and **kwargs to cater for any additional arguments that may be passed in
    #When overriding the django save() method, you should pass in *args and **kwargs
    def save(self, *args, **kwargs): #Here we will specify our own save details, by doing so we will overwrite the defaults from the parent class (models.Model...i think is the parent class or its Profile)
        super().save(*args, **kwargs) #here we run the save method of our parent class

        #Next we must grab the image, then resize it
        img = Image.open(self.image.path) #gets the image, using the pillow library

        if img.height > 300 or img.width > 300: #if image width or height is more than 300 pixels
            output_size = (300, 300) #output_size is a tuple of 300, 300 which will be use to resize image

            img.thumbnail(output_size) #resize image as thumbnailn size specified by "output_size"
            img.save(self.image.path) #"self.image.path" will be the same save location because we want to overwrite the original image with this resized image