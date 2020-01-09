from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Image,Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'caption', 'image')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'profile_photo']



# name = models.CharField(max_length =200)
# caption = models.CharField(max_length =200)
# description = models.TextField()
# image = models


# name = models.CharField(blank=True, max_length=120)
# bio = models.TextField()
# profile_photo = mod
