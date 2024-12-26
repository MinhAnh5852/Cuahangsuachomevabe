from django.shortcuts import render
from . import views

# Create your views here.
def sanpham(request):
    return render(request,'Sanpham/sanpham.html')