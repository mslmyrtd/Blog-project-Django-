from django.shortcuts import render

# Create your views here.
def post_create(request):
    return render (request,"blog/post_create.html")