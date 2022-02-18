from django.urls import path
from .views import home,register,user_login,user_logout

 
 
urlpatterns = [
    
     
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('logout/', user_logout, name="logout"),
    path('login/', user_login, name="user_login"),
    path('profile', home, name="profile"),
    path('create', home, name="create"),

    
]