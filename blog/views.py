from django.shortcuts import render,redirect
from .forms import PostForm,CommentForm
from .models import Post,Like,PostView
import os
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

def details(request,id):
    post=Post.objects.get(id=id)
    form=CommentForm()
    if request.user.is_authenticated:
        view_qs=PostView.objects.filter(author=request.user,post=post)
        if not view_qs:
            PostView.objects.create(author=request.user, post=post)
        if request.method=="POST":
            form=CommentForm(request.POST)
            if form.is_valid():
                comment=form.save(commit=False)
                comment.author=request.user
                comment.post=post
                comment.save()
                return redirect("details" ,id=id)
   
    context = {
        "post": post,
        "form": form
    }    
    return render(request, "blog/details.html", context)

def delete(request,id):
    post=Post.objects.get(id=id)
    if request.method=="POST":
        # os.remove(post.image.path)
        post.delete()
        return redirect("home")
    return render(request, "blog/delete.html", {"post":post}) 


def update(request,id):
    post=Post.objects.get(id=id)
    form=PostForm(instance=post)
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES,instance=post )
        if form.is_valid():
            form.author=request.user
            form.last_updated=Post.last_updated
            form.save()
            return redirect("home")
    context = {
        "form": form,
        "post":post
    }
    return render(request, "blog/update.html", context)

def post_like(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            post=Post.objects.get(id=id)
            like_qs=Like.objects.filter(author=request.user,post=post)
            if like_qs:
                like_qs[0].delete()
            else:
                Like.objects.create(author=request.user,post=post)
    return redirect("details",id=id)
            
