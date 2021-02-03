from django.contrib import admin
from .models import (Category,User,Wallpapers,Popularity,Likes,Favourite)
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header='Admin Tutorial Dashbord'

admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Wallpapers)
admin.site.register(Popularity)
admin.site.register(Likes)
admin.site.register(Favourite)