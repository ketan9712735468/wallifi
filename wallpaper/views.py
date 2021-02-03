from django.shortcuts import render
from .models import (Category,User,Wallpapers,Popularity,Likes,Favourite)
from .serializers import (CategorySerializer,UserSerializer,WallpapersSerializer,PopularitySerializer,LikesSerializer,FavouriteSerializer)
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def categorylist(request):
    query=Category.objects.all()
    serializer=CategorySerializer(query,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def categorydetail(request,pk):
    query=Category.objects.get(id=pk)
    serializer=CategorySerializer(query,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def categorycreate(request):
    serializer=CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['POST'])
def categoryupdate(request,pk):
    query=Category.objects.get(id=pk)
    serializer=CategorySerializer(instance=query,data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['DELETE'])
def categorydelete(request,pk):
    query=Category.objects.get(id=pk)
    query.delete()
    return Response("It's succsesfully delete!")

@api_view(['GET'])
def userlist(request):
    query=User.objects.all()
    serializer=UserSerializer(query,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userdetail(request,pk):
    query=User.objects.get(id=pk)
    serializer=UserSerializer(query,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def usercreate(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['POST'])
def userupdate(request,pk):
    query=User.objects.get(id=pk)
    serializer=UserSerializer(instance=query,data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['DELETE'])
def userdelete(request,pk):
    query=User.objects.get(id=pk)
    query.delete()
    return Response("It's succsesfully delete!")

@api_view(['GET'])
def wallpaperlist(request):
    query=Wallpapers.objects.all()
    serializer=WallpapersSerializer(query,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def wallpaperdetail(request,pk):
    query=Wallpapers.objects.get(id=pk)
    serializer=WallpapersSerializer(query,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def wallpapercreate(request):
    serializer=WallpapersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['POST'])
def wallpaperupdate(request,pk):
    query=Wallpapers.objects.get(id=pk)
    serializer=WallpapersSerializer(instance=query,data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['DELETE'])
def wallpaperdelete(request,pk):
    query=Wallpapers.objects.get(id=pk)
    query.delete()
    return Response("It's succsesfully delete!")

@api_view(['GET'])
def popularitylist(request):
    query=Popularity.objects.all()
    serializer=PopularitySerializer(query,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def popularitydetail(request,pk):
    query=Popularity.objects.get(id=pk)
    serializer=PopularitySerializer(query,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def popularitycreate(request):
    serializer=PopularitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['POST'])
def popularityupdate(request,pk):
    query=Popularity.objects.get(id=pk)
    serializer=PopularitySerializer(instance=query,data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['DELETE'])
def popularitydelete(request,pk):
    query=Popularity.objects.get(id=pk)
    query.delete()
    return Response("It's succsesfully delete!")

@api_view(['GET'])
def likeslist(request):
    query=Likes.objects.all()
    serializer=LikesSerializer(query,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def likesdetail(request,pk):
    query=Likes.objects.get(id=pk)
    serializer=LikesSerializer(query,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def likescreate(request):
    serializer=LikesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['POST'])
def likesupdate(request,pk):
    query=Likes.objects.get(id=pk)
    serializer=LikesSerializer(instance=query,data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['DELETE'])
def likesdelete(request,pk):
    query=Likes.objects.get(id=pk)
    query.delete()
    return Response("It's succsesfully delete!")

@api_view(['GET'])
def favouritelist(request):
    query=Favourite.objects.all()
    serializer=FavouriteSerializer(query,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def favouritedetail(request,pk):
    query=Favourite.objects.get(id=pk)
    serializer=FavouriteSerializer(query,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def favouritecreate(request):
    serializer=FavouriteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['POST'])
def favouriteupdate(request,pk):
    query=Favourite.objects.get(id=pk)
    serializer=FavouriteSerializer(instance=query,data=request.data)
    if serializer.is_valid():
        serializer.save()
        data['ResponseCode']=0
        data['ResponseMessage']='Create successful'
        return Response(data=data)
    else:
        data['ResponseCode']=1
        data['ResponseMessage']='something want wrong'
    return Response(serializer.data)

@api_view(['DELETE'])
def favouritedelete(request,pk):
    query=Favourite.objects.get(id=pk)
    query.delete()
    return Response("It's succsesfully delete!")