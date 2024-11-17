from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/create/', views.new_order, name="new_orders"),
    path('orders/<int:id>/edit/', views.edit_order, name="edit_orders"),
    path('orders/<int:id>/delete/', views.delete_order, name="delete_orders"),
]