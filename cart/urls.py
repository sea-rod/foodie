from django.urls import path
from .views import list_cart_items, add_to_cart_view, ItemDeleteView

urlpatterns = [
    path("", list_cart_items, name="list_cart"),
    path("add/", add_to_cart_view, name="add_cart"),
    path("<int:pk>/delete", ItemDeleteView.as_view(), name="delete_cart"),
]
