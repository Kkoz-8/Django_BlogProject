"""Blog_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # include does not send through what has already been matched in the url, important to remember
    path("", include("blog.urls")), #the blog folder, include the urls.py file via "blog.urls"
    #so from front end, matches from url "blog/" then send any further remaining path (e.g remaining path "about/") from the url for futher processing in urls.py file in blog directory
    #path("blog_dev/", include("blog.urls")) #not used atm
    path("register/", user_views.register, name = "users-register"),
    path("profile/", user_views.profile, name = "users-profile"),
    path("login/", auth_views.LoginView.as_view(template_name = "users/login.html"), name = "users-login"), #".LoginView.as_view()" function handles the user authentication. This is a built in Django function. Path to html file within function parentheses.
    path("logout/", auth_views.LogoutView.as_view(template_name = "users/logout.html"), name = "users-logout"),
    path('admin/', admin.site.urls)
]

#Only add the following if we are in debug mode #See main project directory for debug mode state in the settings.py file
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #adding "MEDIA_URL" and "MEDIA_ROOT" to the urlpatterns, THIS ALLOWS OUR MEDIA FILES TO WORK WITHIN THE BROWSER!