from unicodedata import name
from django import views
from django.urls import path
from blog.views import post_create
from users.views import home
from .views import post_create
urlpatterns=[
    path("", home, name="home"),
    # path("post_create", post_create, name="post")
]
