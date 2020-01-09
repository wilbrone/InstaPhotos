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


    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Image(models.Model):
    """docstring for Image."""

    name = models.CharField(max_length =200)
    caption = models.CharField(max_length =200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateTimeField(auto_now_add = True, null = True)


    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return f"/post/{self.id}"

    @property
    def get_all_comments(self):
        return self.comments.all()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.user.name} Image'


class Comments(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Post'

    class Meta:
        ordering = ["-pk"]


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'
