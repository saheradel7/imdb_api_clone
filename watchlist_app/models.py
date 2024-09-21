from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
from django.contrib.auth.models import User
# Create your models here.

class StreamPlatform(models.Model):
    name =models.CharField( max_length=50)
    about = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.TextField(max_length= 200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,related_name="watch_list")
    active = models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    review_user = models.ForeignKey(User , on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)])
    description = models.CharField(max_length=200, null= True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    watch_list = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    
    def __str__(self):
        return f"{self.rating}" +" "+ self.watch_list.title