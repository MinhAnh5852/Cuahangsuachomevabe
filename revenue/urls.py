from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='revenue_dashboard'),
    path('list/', views.revenue_list, name='revenue_list'),
    path('int:revenue_id/', views.revenue_detail, name='revenue_detail'),
]