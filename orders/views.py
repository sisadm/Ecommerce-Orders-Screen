from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages

from orders.models import Order

# Create your views here.


def orders_list(request):
    orders = Order.objects.all()

    return HttpResponse(f"List of orders: {orders}")