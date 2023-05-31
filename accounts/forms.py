from django.contrib.auth.forms import (
    UserCreationForm,
    UsernameField,
    AuthenticationForm,
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Username",
                "class": "col-7",
            }
        )
    )

    email = forms.EmailField(
        label=("Email"),
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "col-7",
            }
        ),
    )

    contact_no = forms.IntegerField(
        label="Contact no.",
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Contact no",
                "class": "col-7",
            }
        ),
    )

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "col-7",
                "placeholder": "Password",
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "col-7",
                "placeholder": "Confirm Password",
            }
        ),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "contact_no")


class CustomLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Username",
                "class": "col-12",
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "placeholder": "password",
                "class": "col-12",
            }
        ),
    )
