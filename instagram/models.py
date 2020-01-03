from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to = 'images/', blank=True)

    def __str__(self):
        return self.full_name

    def save_editor(self):
        self.save()




class Comments(models.Model):
    coment = models.CharField(max_length =200)

    def __str__(self):
        return self.name



class Image(models.Model):
    """docstring for Image."""

    name = models.CharField(max_length =200)
    caption = models.CharField(max_length =200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank=True)
    likes = models.CharField(max_length =200)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
