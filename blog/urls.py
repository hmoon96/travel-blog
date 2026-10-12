from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("blog/<str:country>/", views.country_posts, name="country_posts"),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
]
