from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def newpost(request):
    form= PostForm()
    if request.method== "POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author=request.user
            form.save()
            return redirect("home")
    context={
        "form":form
        
        
    }
    return render(request, "blog/newpost.html", context)


def postlist(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "users/home.html", context)   


