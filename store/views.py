from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from home.models import Films

# Create your views here.
def single(request, movie_name):
    films = Films.objects.filter(name=movie_name).first
    context = {'films' : films}
    return render(request, 'moviesingle.html', context)