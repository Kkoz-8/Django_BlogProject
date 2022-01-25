from django.shortcuts import render, redirect #also need redirect to redirect user to another page after doing something
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages #display a flash message to screen, e.g, Account Created >_>
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST": # from websiste, register link, if the submit button is clicked.
        form = UserRegisterForm(request.POST) #form is created, inclusive of user input from front end
        if form.is_valid(): #django does back end checks to verify if user already exists, passwords match, etc..
            form.save() #this line here will tell django to automatically save user, hash the password etc.. if username is valid and passwords match
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username} ")
            return redirect("blog-home")
    else:
        form = UserRegisterForm() #Default built in form from django!

    return render(request, "users/register.html", {"form": form})


@login_required #Decorator to modify function "profile", basically you must log in to view user's profile page
def profile(request):

    if request.method == "POST":
        #"request.POST" retrieves the data the user entered into the form
        #"request.FILES" retrieves any file data if there is any, e.g, an image file. 
        #"instance = request.user" will populate the form with the current user information
        user_form = UserUpdateForm(request.POST, instance = request.user) #variable "user_form" to reference an instance of the form "UserUpdateForm"
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile) #variable "profile_form" to reference an instance of the form "ProfileUpdateForm"
        
        if user_form.is_valid() and profile_form.is_valid(): # checking if the data entered by user is valid for both forms
            user_form.save() #".save()" will save and update the data to the backend, and also prompt a post_save() signal. #see "signals.py" file to better understand. #There are receivers that are listening for a signal
            profile_form.save()
            messages.success(request, f"Profile Updated Successfully")
            return redirect("users-profile")

    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance = request.user.profile)

    passing_value = {
        "uform": user_form,
        "pform": profile_form
    }

    return render(request, "users/profile.html", passing_value)





"""message types"""
#messages.debug
#messages.info
#messages.success
#messages.warning
#messages.error