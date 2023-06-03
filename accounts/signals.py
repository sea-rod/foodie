from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomerAddress


@receiver(post_save, sender=get_user_model())
def create_cutomer_address(sender, instance, created, **kwargs):
    if created:
        CustomerAddress.objects.create(user=instance)
