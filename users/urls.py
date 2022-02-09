from django.urls import path
from .views import register,logout,login
urlpatterns = [
    
    path('register/', register, name='register' ),
    path('logout/', logout, name='logout' ),
    path('login/', login, name='login'),
]