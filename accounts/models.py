from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    contact_no = models.CharField(max_length=12)

    def get_absolute_url(self):
        return reverse_lazy("home")


class CustomerAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    house_no = models.CharField(max_length=10)
    ward = models.CharField(max_length=255, null=True)
    village_city = models.CharField(null=True, max_length=255)
    taluka = models.CharField(null=True, max_length=255)
    landmark = models.CharField(null=True, max_length=255)
    pincode = models.PositiveIntegerField(null=True)

    def get_absolute_url(self):
        return reverse_lazy("home")

    def __str__(self):
        return self.user.username
