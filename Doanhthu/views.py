from django.shortcuts import render
from . import views
# Create your views here.

def get_dt(request):
    return render(request,'Doanhthu/doanhthu.html')