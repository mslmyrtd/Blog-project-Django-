from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profil_pic=models.ImageField(upload_to="pofile_pic",blank=True)
    bio=models.TextField()
    