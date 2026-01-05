from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField( max_length=50, null=False)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    post_title = models.CharField(max_length=250, null = False)
    post_category  = models.ForeignKey(Category,on_delete=models.CASCADE)
    post_text = models.TextField(null =True)

# class Resources(models.Model):

# to store logs
# models.py
from django.db import models

class RequestLog(models.Model):
   # user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    view_name = models.CharField(max_length=100)
    method = models.CharField(max_length=10)
    duration = models.FloatField()  # in seconds
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.view_name}  at {self.timestamp}"

