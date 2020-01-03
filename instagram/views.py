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
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})


# @login_required(login_url='/accounts/login/')
def all_photos(request):
    title = "You are Home atlast"

    return render(request, 'all-pics/index.html', {"title":title})

def logout(request):
    pass
