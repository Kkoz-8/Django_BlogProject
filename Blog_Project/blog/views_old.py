from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): #Homepage #A parameter is necessary! A request is passed from the front end
    return HttpResponse("<h1>Blog Home</h1>") #Homepage Header

def about(request): #Aboutpage #A parameter is necessary! A request is passed from the front end
    return HttpResponse("<h1>Blog About</h1>")