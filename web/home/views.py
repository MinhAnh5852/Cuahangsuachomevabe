# home/views.py

from django.shortcuts import render

def get_home(request):
    return render(request, 'home.html')