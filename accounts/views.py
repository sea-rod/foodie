from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomLoginForm


class SignupView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    success_url = reverse_lazy("home")
