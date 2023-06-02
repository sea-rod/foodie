from typing import Any
from django.contrib.auth.views import LoginView
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, authenticate, login
from .models import CustomerAddresss
from .forms import (
    CustomUserCreationForm,
    CustomLoginForm,
    CustomChangeUserForm,
    CustomerAddressForm,
)


class SignupView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"

    def get_success_url(self) -> str:
        return reverse_lazy("address_settings")

    def form_valid(self, form) -> HttpResponse:
        valid = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password1"),
        )
        print(user)
        login(self.request, user)
        CustomerAddresss.objects.create(
            user=get_user_model().objects.get(pk=self.object.id)
        )
        return valid


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    success_url = reverse_lazy("home")


class ChangeUserView(UpdateView):
    model = get_user_model()
    template_name = "registration/changeUser.html"
    form_class = CustomChangeUserForm
    # fields = ["username", "email", "contact_no"]


def AddressUpdateView(request: HttpRequest):
    address = CustomerAddresss.objects.get(user=request.user)
    if request.method == "POST":
        address.pincode = request.POST["pincode"]
        address.village_city = request.POST["village_city"]
        address.ward = request.POST["ward"]
        address.save()
        return redirect("home")

    dic = {
        "pincode": address.pincode,
        "village_city": address.village_city,
        "ward": address.ward,
    }

    context = {"form": CustomerAddressForm(initial=dic)}

    return render(request, "settings.html", context)
