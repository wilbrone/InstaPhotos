from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, request
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime as dt

from .models import Image
from instagram.forms import SignUpForm, LoginForm, UploadImage



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # user = User.objects.create_user(username = username, password1 = password, email = email)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # user = User.objects.create_user(username = username, password1 = password, email = email)
#             # form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             # login(request, user)
#             users = User.objects.get(password = password1)
#             return redirect('index')
#     else:
#         form = LoginForm()
#
#     return render(request, 'registration/login.html', {'form': form})


# @login_required(login_url='/accounts/login/')
def all_photos(request):
    photos = Image.get_image()
    return render(request, 'all-pics/index.html', {'photos':photos})


def user_profile(request):
    pass



def logout(request):
    pass
