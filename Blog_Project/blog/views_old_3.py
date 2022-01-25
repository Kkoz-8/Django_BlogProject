from django.shortcuts import render #renders the html for you, and just returns the already rendered template
from .models import Post #the dot "." means current directory, models is the models.py file and Post is the class (aka model) within the file


def home(request): #request is basically passed from the front end user, this is a mandatory parameter
    context = { 
        "posts": Post.objects.all() #from models.py file, class/model Post
    }
    return render(request, "blog_directory/home.html", context) #render also requires the request as the first argument, also do not need to specify the templates folders because Django auto searches and expects the templates folder
    # the dictonary "context" is passed to the "home.html" template in the "blog_directory" directory

def about(request): #request is basically passed from the front end user, this is a mandatory parameter
    return render(request, "blog_directory/about.html", {"title": "About"}) #render also requires the request as the first argument, also do not need to specify the templates folders because Django auto searches and expects the templates folder