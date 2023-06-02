from django.urls import path
from .views import SignupView, CustomLoginView, ChangeUserView, AddressUpdateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<int:pk>/profile/", ChangeUserView.as_view(), name="profile"),
    path("settings/", AddressUpdateView, name="address_settings"),
]
