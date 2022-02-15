from multiprocessing import context
from django.shortcuts import render
from .models import Card
# Create your views here.
def post_create(request):
    return render (request,"blog/post_create.html")

def post_list(request):
    posts= Card.objects.all()
    context={
        "posts":posts
    }
    return render (request,"blog/post_list.html",context)