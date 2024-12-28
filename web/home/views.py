from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse 
from .models import Order 

def get_home(request):
    return render(request, 'order_detail.html')
def get_home1(request):
    return render(request, 'order_list.html')

# Create your views here.
class OrderListView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        orders = Order.objects.filter(user=request.user)
        return render(request, 'orders/order_list.html', {'orders': orders})

class OrderDetailView(View):
    def get(self, request, order_id):
        if not request.user.is_authenticated:
            return redirect('login')

        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=404)

        return render(request, 'orders/order_detail.html', {'order': order})