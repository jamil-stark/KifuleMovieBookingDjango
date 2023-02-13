from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Films
from store.models import Order, OrderItem

def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders' : orders
    }
    return render(request, "ordersindex.html", context)