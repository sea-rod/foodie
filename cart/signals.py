from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Cart, Items


@receiver(post_delete, sender=Items)
def item_delete(sender, instance, **kargs):
    cart = instance.cart_id
    cart.total_price -= instance.food_id.price * instance.quantity
    cart.save()
