from django.db import models
class Category():
    pass
# Create your models here.
class Post(models.Model):
    OPTIONS=(
        ("d","Draft"),
        ("p","Published"),
    )
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField()
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    last_updated=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(auto_now_add=True)
    # author=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=10, choices=OPTIONS,default="d")
    slug=