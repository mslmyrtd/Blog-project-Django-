from unicodedata import name
from django import views
from django.urls import path
from .views import post_list,post_create
from users.views import home
from .views import post_create
urlpatterns=[
    path("", home, name="home"),
    path("create/", post_create, name="post"),
    path("list", post_list, name="list"),
]
