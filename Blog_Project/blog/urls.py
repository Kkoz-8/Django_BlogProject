from django.urls import path
from . import views #the dot "." represents current directory
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)


urlpatterns = [
    #path("", views.home, name = "blog-home"), #leaving it blank to specify it as homepage #views.home is the function home from the views.py file #give it a name for easy future reference
    path("", PostListView.as_view(), name = "blog-home"), #when using class based views "PostListView", we must convert the class into a view using method "as_view()"
    path("post/create/", PostCreateView.as_view(), name = "post-create"),
    path("user/<str:username>", UserPostListView.as_view(), name = "user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name = "post-detail"), #"post/<int:pk>/" we can pass a vairable "post" to a url in django. <int:pk> is integer for pk "primary key" which is what django looks for by default
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name = "post-update"), #url for user to update a post, filter by primary key of the post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name = "post-delete"), #url for user to delete a post, filter by primary key of the post
    path("about/", views.about, name = "blog-about") #front end /blog/about/ path references here. then calls function about from views.py file #name is the name for this url path. can reference this url by its name
]


#class based views looks for templates with a specific naming convention:
#name of the app, name of model_viewtype.html
    #in this case: "blog_directory/post_list.html"
#However we can change the template that we want class based views to use