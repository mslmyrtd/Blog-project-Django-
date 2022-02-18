from django.urls import path
from .views import home,register,user_login

 
 
urlpatterns = [
    
     
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('logout', home, name="logout"),
    path('login', user_login, name="login"),
    path('profile', home, name="profile"),
    path('create', home, name="create"),

    
]