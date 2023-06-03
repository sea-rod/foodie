from django.contrib import admin
from .models import CustomUser, CustomerAddress

admin.site.register(CustomUser)
admin.site.register(CustomerAddress)
