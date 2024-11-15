from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages

from orders.models import Order
from .forms import OrderForm

# Create your views here.


# listing all orders
def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

# new order
def new_order(request):

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your order was placed")
            form = OrderForm()
    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {'form': form})



def edit_order(request):

    return HttpResponse("Hello edit Order")


def delete_order(request):

    return HttpResponse("Hello delete Order")