from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from food.models import Food
from .models import Cart, Items


@login_required()
def add_to_cart_view(request: HttpRequest):
    if request.method == "POST":
        food_id = request.POST["food"]
        quantity = request.POST["quantity"]
        food_id = Food.objects.get(id=food_id)

        cart_id = Cart.objects.get(user=request.user)
        cart_id.total_price += food_id.price * int(quantity)
        cart_id.save()

        Items.objects.create(cart_id=cart_id, food_id=food_id, quantity=quantity)

        return redirect("menu")

    return render(request, "add.html")


@login_required()
def list_cart_items(request: HttpRequest):
    cart = Cart.objects.get(user=request.user)

    context = {"cart_list": cart}
    return render(request, "cart.html", context)


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Items
    template_name = "cart.html"
    success_url = reverse_lazy("list_cart")

    def test_func(self) -> bool | None:
        obj = self.get_object()
        user = Cart.objects.get(pk=obj.cart_id.id).user
        return self.request.user == user
