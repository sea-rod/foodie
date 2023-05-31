from django.urls import path
from .views import SignupView, CustomLoginView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
]
