from django.shortcuts import render #renders the html for you, and just returns the already rendered template
from .models import Post #the dot "." means current directory, models is the models.py file and Post is the class (aka model) within the file

#Dummy Data
posts_list = [
{"author": "Scott Johnson",
"title": "Blog Post 1",
"content": "First Post Desu",
"date_posted": "2020-08-19"},

{"author": "Super Saiyan",
"title": "Blog Post 2",
"content": "Second Post Desu",
"date_posted": "2020-12-01"}
]

# Create your views here.
def home(request): #request is basically passed from the front end user, this is a mandatory parameter
    context = { #create dictionary "context" with key "posts" and value is "posts_list" created at top of this file
        "posts": posts_list
    }
    return render(request, "blog_directory/home.html", context) #render also requires the request as the first argument, also do not need to specify the templates folders because Django auto searches and expects the templates folder
    # the dictonary "context" is passed to the "home.html" template in the "blog_directory" directory

def about(request): #request is basically passed from the front end user, this is a mandatory parameter
    return render(request, "blog_directory/about.html", {"title": "About"}) #render also requires the request as the first argument, also do not need to specify the templates folders because Django auto searches and expects the templates folder