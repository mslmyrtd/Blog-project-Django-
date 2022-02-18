from django.urls import path
from .views import home,register,user_login,user_logout,profile
from blog.views import postlist
 
 
urlpatterns = [
    
     
    path('', postlist, name="home"),
    path('register/', register, name="register"),
    path('logout/', user_logout, name="logout"),
    path('login/', user_login, name="user_login"),
    path('profile', profile, name="profile"),
    path('create', home, name="create"),

    
]