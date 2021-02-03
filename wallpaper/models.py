from django.db import models
from PIL import Image

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=40)
    postdate=models.DateField()
    modifydate=models.DateField()
    status=models.CharField(max_length=40)
    image=models.ImageField(upload_to='Images/',max_length=255,null=True)
  

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img= Image.open(self.image.path)

        if img.height > 300 or img.weight < 300:
            outuput_size =(300,300)
            img.thumbnail(outuput_size)
            img.save(self.image.path)

    def __str__(self):
        return self.name

class User(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Wallpapers(models.Model):
    categoryId=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    postdate=models.DateField()
    modifydate=models.DateField()
    size=models.IntegerField()
    ratio=models.IntegerField()
    image=models.ImageField(upload_to='Images/',max_length=255,null=True)
    
    def __str__(self):
        return self.title

class Popularity(models.Model):
    wallpaperId=models.ForeignKey(Wallpapers,on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    postdate=models.DateField()
    modifydate=models.DateField()
    
    def __str__(self):
        return self.title

class Likes(models.Model):
    likesId=models.ForeignKey(User,on_delete=models.CASCADE)
    size=models.IntegerField()
    ratio=models.IntegerField()
    postdate=models.DateField()
    modifydate=models.DateField()

class Favourite(models.Model):
    favouriteId=models.ForeignKey(User,on_delete=models.CASCADE)
    size=models.IntegerField()
    ratio=models.IntegerField()
    postdate=models.DateField()
    modifydate=models.DateField()
