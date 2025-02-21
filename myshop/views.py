
from django.shortcuts import render

def order_view(request):
    return render(request, 'order.html')