from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) #can now see on the admin login, the info from the Post model in models.py #register is lowercase