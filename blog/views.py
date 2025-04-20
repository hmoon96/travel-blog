from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


# Blog posts view
def blog(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/blog.html', {'posts': posts})