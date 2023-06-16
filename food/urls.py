from django.urls import path
from .views import index, Menu, about


urlpatterns = [
    path("", index, name="home"),
    path("menu/", Menu.as_view(), name="menu"),
    path("about/", about, name="about"),
]
