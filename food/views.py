from django.views.generic import ListView
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def menu(request):
    return render(request, "menu.html")
