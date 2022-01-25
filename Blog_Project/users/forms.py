from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)

    #"Meta" has to use uppercase M
    class Meta: #Class "Meta" gives us a nested namespace for configurations, and keeps the configurations in one place
        #Next we specify what models would be affected
        model = User #specify the model (in this case "User") you want the form to interact with

        #Next specify what fileds you want on the form, in what order
        fields = ["username", "email", "password1", "password2"] #password confirmation is "password2"


class UserUpdateForm(forms.ModelForm): # inherit from django "forms.ModelForm" parent class
    email = forms.EmailField(required = True)

    class Meta:
        model = User #what model we want to interact with

        fields = ["username", "email"] #what fields we want on the form


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile #what model we want to interact with
        fields = ["image"] #what fields we want on the form