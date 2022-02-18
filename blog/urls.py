from django.urls import path
from .views import newpost,details,delete,update
urlpatterns = [

    path('newpost/',newpost, name="newpost" ),
    path('details/<int:id>',details, name="details" ),
    path('delete/<int:id>',delete, name="delete" ),
    path('update/<int:id>',update, name="update" ),
]