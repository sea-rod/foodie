from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm


class SignupView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = "signup.html"
