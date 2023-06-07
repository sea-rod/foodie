from django.db import models
from django.contrib.auth import get_user_model
from food.models import Food


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return self.user.username


class Items(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()
