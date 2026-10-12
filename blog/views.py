from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


# Countries view
def blog(request):
    countries = (
        Post.objects.exclude(country="")
        .values_list("country", flat=True)
        .distinct()
        .order_by("country")
    )
    return render(request, "blog/blog.html", {"countries": countries})

# Country-specific posts view
def country_posts(request, country):
    posts = Post.objects.filter(country__iexact=country).order_by("-date_posted")
    if not posts.exists():
        raise Http404("No posts found for this country.")

    return render(
        request,
        "blog/country_posts.html",
        {"country": country, "posts": posts},
    )


# About page view
def about(request):
    return render(request, 'blog/about.html')