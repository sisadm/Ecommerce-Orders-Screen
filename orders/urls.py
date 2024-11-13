from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/create/', views.new_order, name="new_orders"),
    path('orders/edit/', views.edit_order, name="edit_orders"),
    path('orders/delete/', views.delete_order, name="delete_orders"),
]