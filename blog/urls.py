from django.urls import path
from .views import newpost,postlist
urlpatterns = [

    path('newpost/',newpost, name="newpost" ),
    # path('postlist/',postlist, name="list" ),
]