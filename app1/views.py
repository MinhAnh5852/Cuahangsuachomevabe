from django.shortcuts import render
from . import views
# Create your views here.

def get_app1(request):
    return render(request,'app1/QLDH.html')