from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, authenticate, login
from .models import CustomerAddress
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
        return valid


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    success_url = reverse_lazy("home")


class ChangeUserView(UpdateView):
    model = get_user_model()
    template_name = "registration/changeUser.html"
    form_class = CustomChangeUserForm
    # fields = ["username", "email", "contact_no"]


@login_required()
def AddressUpdateView(request: HttpRequest):
    address = CustomerAddress.objects.get(user=request.user)
    if request.method == "POST":
        address.house_no = request.POST["house_no"]

        address.pincode = request.POST["pincode"]
        address.ward = request.POST["ward"]
        address.village_city = request.POST["village_city"]
        address.taluka = request.POST["taluka"]
        address.landmark = request.POST["landmark"]
        address.save()
        return redirect("home")

    dic = {
        "house_no": address.house_no,
        "pincode": address.pincode,
        "ward": address.ward,
        "village_city": address.village_city,
        "taluka": address.taluka,
        "landmark": address.landmark,
    }

    context = {"form": CustomerAddressForm(initial=dic)}

    return render(request, "settings.html", context)
