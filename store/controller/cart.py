import json
from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Films
from store.models import ToWatch
from django.http import JsonResponse

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            fil_id = int(request.POST.get('film_id'))
            film_check = Films.objects.get(id=fil_id)
            if (film_check):
                if(ToWatch.objects.filter(user=request.user.id, film_id=fil_id)):
                    return JsonResponse({'status': "Film added already"})
                else:
                    ToWatch.objects.create(user=request.user, film_id = fil_id, number_of_tickets = 1)
                    return JsonResponse({'status': "Film added successfully"})
            else:
                return JsonResponse({'status': "Film not found"})
        else:
            return JsonResponse({'status': "Login to continue"})

    else:
        return redirect('/')


def showtickets(request):
    ticket = ToWatch.objects.filter(user=request.user)
    context = {'ticket' : ticket}
    return render(request, "ticket.html", context)

def deletecartitem(request):
    if request.method == 'POST':
        fil_id = int(request.POST.get('film_id'))
        if(ToWatch.objects.filter(user=request.user.id, film_id=fil_id)):
            cartitem = ToWatch.objects.get(film_id=fil_id, user=request.user)
            cartitem.delete()
            return JsonResponse({'status': "Film deleted Successfully"})
    return redirect('/')