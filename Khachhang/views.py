from django.shortcuts import render
from . import views
# Create your views here.

def get_kh(request):
    return render(request,'Khachhang/khachhang.html')                                                    