from django.db import models

# Create your models here.
class Card(models.Model):
    
    title=models.CharField(max_length=15)
    description=models.TextField()
    
def __str__(self):
    return self.title
