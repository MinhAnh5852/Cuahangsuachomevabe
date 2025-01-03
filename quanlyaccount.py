from django.db import models
from django.contrib.auth.models import AbstractUser
#nguoi dung
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

from django import forms
from .models import User
#form dang ky
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

from django.contrib import admin
from .models import User

admin.site.register(User)

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
