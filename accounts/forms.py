from django.contrib.auth.forms import (
    UserCreationForm,
    UsernameField,
    AuthenticationForm,
    UserChangeForm,
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation, get_user_model
from django import forms
from .models import CustomUser, CustomerAddress


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
        model = get_user_model()
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


class CustomChangeUserForm(UserChangeForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Username",
                "class": "col-6",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "autofocus": True,
                "placeholder": "Email",
                "class": "col-6",
            }
        )
    )

    contact_no = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "autofocus": True,
                "placeholder": "Contact No.",
                "class": "col-6",
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "contact_no"]


class CustomerAddressForm(forms.ModelForm):
    pincode = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "pincode",
                "max": 999999,
            }
        )
    )
    house_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "House.No.",
                "maxlength": "6",
            }
        )
    )

    ward = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ward",
            }
        )
    )

    village_city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "village/city",
            }
        )
    )

    taluka = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "taluka",
            }
        )
    )
    landmark = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "landmark",
            }
        )
    )

    class Meta:
        model = CustomerAddress
        fields = ["house_no", "ward", "village_city", "taluka", "landmark", "pincode"]
