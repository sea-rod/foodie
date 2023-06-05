from django.views.generic import ListView
from django.shortcuts import render
from .models import FoodCategory


def index(request):
    return render(request, "index.html")


class Menu(ListView):
    model = FoodCategory
    template_name = "menu.html"
    context_object_name = "food_category"
