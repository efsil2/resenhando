from django.shortcuts import render
from django.utils import timezone
from .models import Films
from .models import Post
from .models import models

def films_list(request):
    film=Films.objects.filter().order_by('name')
    return render(request, 'controller/films_list.html',{'film':film})

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'controller/post_list.html', {'posts':posts})
