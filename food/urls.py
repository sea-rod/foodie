from django.urls import path
from .views import index, Menu


urlpatterns = [
    path("", index, name="home"),
    path("menu/", Menu.as_view(), name="menu"),
]
