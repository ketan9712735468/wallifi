from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('category-list',categorylist),
    path('category-detail/<str:pk>',categorydetail),
    path('category-create',categorycreate),
    path('category-update/<str:pk>',categoryupdate),
    path('category-delete/<str:pk>',categorydelete),
    path('user-list',userlist),
    path('user-detail/<str:pk>',userdetail),
    path('user-create',usercreate),
    path('user-update/<str:pk>',userupdate),
    path('user-delete/<str:pk>',userdelete),
    path('wallpaper-list',wallpaperlist),
    path('wallpaper-detail/<str:pk>',wallpaperdetail),
    path('wallpaper-create',wallpapercreate),
    path('wallpaper-update/<str:pk>',wallpaperupdate),
    path('wallpaper-delete/<str:pk>',wallpaperdelete),
    path('popularity-list',popularitylist),
    path('popularity-detail/<str:pk>',popularitydetail),
    path('popularity-create',popularitycreate),
    path('popularity-update/<str:pk>',popularityupdate),
    path('popularity-delete/<str:pk>',popularitydelete),
    path('like-list',likeslist),
    path('like-detail/<str:pk>',likesdetail),
    path('like-create',likescreate),
    path('like-update/<str:pk>',likesupdate),
    path('like-delete/<str:pk>',likesdelete),
    path('favourite-list',favouritelist),
    path('favourite-detail/<str:pk>',favouritedetail),
    path('favourite-create',favouritecreate),
    path('favourite-update/<str:pk>',favouriteupdate),
    path('favourite-delete/<str:pk>',favouritedelete),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
