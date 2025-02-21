from django.shortcuts import render
from django.db.models import Sum
from .models import Revenue

def dashboard(request):
    total_revenue = Revenue.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'revenue/dashboard.html', {'total_revenue': total_revenue})

def revenue_list(request):
    revenues = Revenue.objects.all()
    return render(request, 'revenue/revenue_list.html', {'revenues': revenues})

def revenue_detail(request, revenue_id):
    revenue = Revenue.objects.get(pk=revenue_id)
    return render(request, 'revenue/revenue_detail.html', {'revenue': revenue})