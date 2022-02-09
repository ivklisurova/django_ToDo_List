from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    bio = models.TextField()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class ToDo(models.Model):
    todo_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=40, default='')
    task_text = models.TextField(max_length=450, default='')
    task_done = models.BooleanField(default=False)
