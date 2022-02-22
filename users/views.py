from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm,ProfileForm
# Create your views here.
def home(request):
    return render(request, "users/home.html")

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    context = {
        'form_user': form
    }

    return render(request, "users/register.html", context)

def user_logout(request):
    
    logout(request)
    return redirect('home')

def user_login(request):

    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            
            login(request, user)
            return redirect('home')
    return render(request, 'users/user_login.html', {"form": form})
def profile(request):
    user = request.user
    form = ProfileForm(instance =user)
    if request.method =="POST":
        form = ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect("home")
    context = {
        "form":form,
        "user":user
    }
    return render(request,"users/profile.html",context)