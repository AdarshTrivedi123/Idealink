from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    category=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

class like_blog(models.Model):
    blog_id=models.IntegerField()
    user_id=models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

class cmnt_blog(models.Model):
    blog_id=models.IntegerField()
    content=models.TextField()
    user_id=models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

class Bookmark_blog(models.Model):
    blog_id=models.IntegerField()
    user_id=models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    content=models.TextField()
    username= models.ForeignKey(User, on_delete=models.CASCADE)
    # user_id=models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
