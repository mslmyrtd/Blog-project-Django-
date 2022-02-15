from django.db import models

# Create your models here.
class Card(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    # category=models.ForeignKey(Category, on_delete=models.PROTECT)
    image=models.ImageField()
    publish_date=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey()
    status=
    
def __str__(self):
    return self.title


