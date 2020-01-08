from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404, HttpResponse, request, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import datetime as dt
# from django.contrib.auth.decorators import login_required

from .models import Image
from instagram.forms import SignUpForm



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
            print("*****success*****")
            return redirect('allPhotos')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})



# @login_required(login_url='login')
def all_photos(request):
    photos = Image.get_image()
    return render(request, 'all-pics/index.html', {'photos':photos})


def user_profile(request):
    pass



def logout(request):
    pass
