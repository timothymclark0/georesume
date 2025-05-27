from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *
# Create your views here.

def view_post(request,year,month,day,slug):
    post = get_object_or_404(Post, 
                            date_posted__year=year,
                            date_posted__month=month, 
                            date_posted__day=day, 
                            slug=slug)
    context = {'post':post}
    return render(request,'post.html', context)

def post_list(request, year=None, month=None, day=None, tag=None):
    posts = get_list_or_404(Post)
    
    context = {'posts': posts}
    return render(request,'post_list.html', context)