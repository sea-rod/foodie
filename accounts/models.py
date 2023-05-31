from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    contact_no = models.CharField(max_length=12)
