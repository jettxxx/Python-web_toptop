from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return render(request, 'users/login.html')


def home(request):
    return render(request, 'users/home.html')


def register(request):
    return render(request, 'users/register.html')


def create(request):
    return render(request, 'users/create.html')
