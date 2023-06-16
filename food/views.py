from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from .models import FoodCategory, Food


def index(request):
    return render(request, "index.html")


class Menu(ListView):
    model = FoodCategory
    template_name = "menu.html"
    context_object_name = "food_category"
    obj = None

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        search = request.GET.get("search", None)
        print(search)
        if search:
            self.obj = Food.objects.filter(name__contains=search)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        if self.obj is not None:
            context = super().get_context_data(**kwargs)
            context[self.context_object_name] = None
            context["food_search"] = self.obj
            context["search_head"] = "No search Result"
            if self.obj:
                context["search_head"] = "Search Results"
            return context

        return super().get_context_data(**kwargs)


def about(request):
    return render(request, "about.html")
