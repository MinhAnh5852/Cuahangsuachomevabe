from django.shortcuts import render

# Create your views here.
def get_order(request):
    return render(request, 'order.html')