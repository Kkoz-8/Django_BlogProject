from django.db import models
from django.utils import timezone #used to get current times etc
from django.contrib.auth.models import User
from django.urls import reverse #reverse returns the full url to a route as a string, whereas redirect directs you to a specific route


class Post(models.Model): #each class will be its own table in the database
    title = models.CharField(max_length = 100)
    content = models.TextField() #No limit when using ".TextField()"
    date_posted = models.DateTimeField(default = timezone.localtime) #when this class "Post" is called, this will give the current time
    author = models.ForeignKey(User, on_delete = models.CASCADE) # ".CASCADE" if user is deleted, delete their posts, but if a post is deleted, do not delete the user

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self): #Here we will have a url to define this object instance
        return reverse("post-detail", kwargs={"pk": self.pk}) #here we will return the url as a string, then the view in views.py will handle the redirect
        #see blog/urls.py for the url with name "post-detail", the url there references a variable and a primary key as: "post/<int:pk>"
        #as such, use kwargs to reference the specific post id via its primary key