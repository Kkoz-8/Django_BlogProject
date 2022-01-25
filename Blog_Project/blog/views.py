from django.shortcuts import render, redirect, get_object_or_404 #renders the html for you, and just returns the already rendered template
from .models import Post #the dot "." means current directory, models is the models.py file and Post is the class (aka model) within the file
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView #importing django built in ListView, DetailView, CreateView, UpdateView, DeleteView classes
)
from django.contrib.auth.mixins import LoginRequiredMixin #basically class "LoginRequiredMixin" adds similar functionality to classes like the @login_required decorator does for functions
from django.contrib.auth.mixins import UserPassesTestMixin #having other classes inherit this class, allows users to only make changes to their own posts
from django.contrib.auth.models import User


def home(request): #request is basically passed from the front end user, this is a mandatory parameter
    context = { 
        "posts": Post.objects.all() #from models.py file, class/model Post
    }
    return render(request, "blog_directory/home.html", context) #render also requires the request as the first argument, also do not need to specify the templates folders because Django auto searches and expects the templates folder
    # the dictonary "context" is passed to the "home.html" template in the "blog_directory" directory


class PostListView(ListView): #create class "PostListView" inheriting from django class "ListView"
    model = Post #from "models.py" import model "Post"
    template_name = "blog_directory/home.html" #"template_name" is a variable inherited that specifies the path of what template you want the view to use
    context_object_name = "posts" #"context_object_name" is also inherited, and it specifies path to context you want passed to your template
    ordering = ["-date_posted"] #will order posts to have most recent post at the top, you can set as ["date_posted"] to have oldest post at the top
    paginate_by = 6 #using the attribute "paginate_by" to specify how many posts should displayed per page


class UserPostListView(ListView):
    model = Post
    template_name = "blog_directory/user_posts.html"
    context_object_name = "posts"
    paginate_by = 6 

    def get_queryset(self):
        #if user exists, capture user to variable "user" else return 404
        user = get_object_or_404(User, username = self.kwargs.get("username")) #we get the object from the model "User" where username is taken from url via "self.kwargs.get("username")"
        return Post.objects.filter(author=user).order_by("-date_posted") #return all posts by author for user captured in variable "user"


class PostDetailView(DetailView): #create class "PostDetailView" inheriting from django class "DetailView"
    model = Post #from "models.py" import model "Post"
    template_name = "blog_directory/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView): #create class "PostDetailView" inheriting from django class "DetailView"
    model = Post #from "models.py" import model "Post"
    template_name = "blog_directory/post_form.html"
    fields = ["title", "content"]

    def form_valid(self, form): #here we over-ride the default "form_valid" method
        #This will be done before user submits the form, that way we won't encounter an author null id error.
        form.instance.author = self.request.user #we set the "form.instance.author" to the person sending the request via "self.request.user"
        return super().form_valid(form) #validate the form, have to use super because form features are inherited from the parent class


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #create class "PostDetailView" inheriting from django class "DetailView"
    model = Post #from "models.py" import model "Post"
    template_name = "blog_directory/post_form.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #method to prevent user from editing posts other than their own
    def test_func(self): #adding this method will test if user logged in is the author of the post they are trying to edit
        post = self.get_object() #get the current post that user is trying to update
        if self.request.user == post.author: #verify if logged in user is the current author of the post
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #create class "PostDetailView" inheriting from django class "DetailView"
    model = Post #from "models.py" import model "Post"
    template_name = "blog_directory/post_confirm_delete.html"
    success_url = "/" #directs user to the home page if they delete a post

    #Allows user to delete their own post, not other user's posts
    def test_func(self):
        post = self.get_object() #get the current post that user is trying to delete
        if self.request.user == post.author: #verify if logged in user is the current author of the post
            return True
        return False
    

def about(request): #request is basically passed from the front end user, this is a mandatory parameter
    return render(request, "blog_directory/about.html", {"title": "About"}) #render also requires the request as the first argument, also do not need to specify the templates folders because Django auto searches and expects the templates folder