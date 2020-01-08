from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Image


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'caption', 'description', 'image',)

# class LoginForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username',  'password1',)
#
# class UploadImage(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('name', 'caption', 'description', 'image')


# name = models.CharField(max_length =200)
# caption = models.CharField(max_length =200)
# description = models.TextField()
# image = models
