from rest_framework import serializers
from .models import (Category,User,Wallpapers,Popularity,Likes,Favourite)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class WallpapersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallpapers
        fields='__all__'

class PopularitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Popularity
        fields='__all__'

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        fields='__all__'

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favourite
        fields='__all__'