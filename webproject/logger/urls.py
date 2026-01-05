#from django.contrib import admin
from django.urls import path
from .views import add_post,list_posts

urlpatterns = [
    path('add_post/',add_post,name ='add'),
    path('list_posts/',list_posts,name ='post_list'),

]