from django.urls import path
from .views import newpost,details,delete,update,post_like
urlpatterns = [

    path('newpost/',newpost, name="newpost" ),
    path('details/<int:id>',details, name="details" ),
    path('delete/<int:id>',delete, name="delete" ),
    path('update/<int:id>',update, name="update" ),
    path('post_like/<int:id>',post_like, name="post_like" ),
]