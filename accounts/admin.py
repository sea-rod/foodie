from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomChangeUserForm, CustomUserCreationForm
from .models import CustomerAddress

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomChangeUserForm
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomerAddress)
