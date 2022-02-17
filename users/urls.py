from django.urls import path
from .views import home

 
 
urlpatterns = [
    
     
    path('', home, name="home"),
    path('register/', home, name="register"),
    path('logout', home, name="logout"),
    path('login', home, name="login"),
    path('profile', home, name="profile"),
    path('create', home, name="create"),

    
]