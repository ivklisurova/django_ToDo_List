from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    about = models.CharField(max_length=200)
    image_url = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
