from django.shortcuts import render,redirect
from .models import Category,Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def add_post(request):

    
    if request.method == "POST":
        


       
        
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, "Post created successfully!")
            #return ("walla")
            return redirect('post_list') 


    else:
        
   


        post_form = PostForm()
    return render(request, 'logger/add_post.html', {'post_form': post_form})


def list_posts (request):
    posts = Post.objects.all()
    return render (request, 'logger/post_list.html', {'posts':posts})