from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='orders_list')
]