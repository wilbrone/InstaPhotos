from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, max_length=120)
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to = 'images/', blank=True)


    def __str__(self):
        return self.bio


    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


    def save_profile(self):
            self.save()


    def delete_profile(self):
        self.delete()


class Comments(models.Model):
    coment = models.CharField(max_length =200)
    trial = models.CharField(max_length =200)

    def __str__(self):
        return self.coment



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
        ordering = ['-pk']

    @classmethod
    def get_image(cls):
        images = cls.objects.all()

        return images
