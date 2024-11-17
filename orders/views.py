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
            return redirect('orders_list')
    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {'form': form})



def edit_order(request, id):
    post = get_object_or_404(Order, pk=id)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Your order was placed")

    else: 
        form = OrderForm(instance=post)

    return render(request, 'orders/order_form.html', {'form': form, 'post': post})


def delete_order(request, id):

    
    order = get_object_or_404(Order, id=id)
    order.delete()
    messages.success(request, "Order has been successfully deleted.")
    return redirect('orders_list')
    
    
