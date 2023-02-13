from cmath import log
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from home.models import Films
from store.models import ToWatch, Order, OrderItem
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User
from django.http import JsonResponse

def index(request):
    cartitems = ToWatch.objects.filter(user=request.user)
    total_price = 0;
    for item in cartitems:
        total_price += item.film.price
    usd_price = total_price * 0.00027
    context = {'cartitems' : cartitems, 'total_price' : total_price, 'usd_price' : usd_price}
    return render(request, "checkout.html", context)

def placeorder(request):
    if request.method == "POST":
        currentuser = User.objects.filter(id=request.user.id).first()

        neworder = Order()
        neworder.user = request.user
        if request.POST.get('payment_mode') != "COD":
            neworder.names = "John"
        else:
            neworder.names = request.POST.get('ticketOwner')
        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')

        cart = ToWatch.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price += item.film.price
        
        neworder.total_price = cart_total_price
        trackno = 'kauki'+str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_number=trackno) is None:
            trackno = 'kauki'+str(random.randint(1111111, 9999999))
        neworder.tracking_number = trackno
        neworder.save()
        neworderitems = ToWatch.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order = neworder,
                film = item.film,
                price=item.film.price
            )
            #to clear user's cart(ToWatch)
            ToWatch.objects.filter(user=request.user).delete()
            messages.success(request, "Your order has been placed")
            pay_mode = request.POST.get('payment_mode')
            if (pay_mode == "paid by RazorPay" or pay_mode == "paid by PayPal"):
                return JsonResponse({'status': "Your order has been placed"})
    return redirect('/store/my-orders')

def proceedtopay1(request):
    cart = ToWatch.objects.filter(user = request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.film.price
    usdpp = total_price * 0.0003
    usdp = int(usdpp)
    return JsonResponse({
        'usdp' : usdp
    })


def orders(request):
    return HttpResponse("My orders Page")