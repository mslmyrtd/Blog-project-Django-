from email.policy import default
from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
def user_directory_path(instance,filename):
    # return "blog/{0}/{1}".format(instance.author.id, filename)
    pass
class Category(models.Model):
    
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural="Categories"
    
# Create your models here.
class Post(models.Model):
    
    OPTIONS=(
        ("d","Draft"),
        ("p","Published"),
    )
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to="img/", blank=True)
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    last_updated=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    status=models.CharField(max_length=10, choices=OPTIONS,default="d")
    
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    
    
class Like(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
class PostView(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(auto_now_add=True)