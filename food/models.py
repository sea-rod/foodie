from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Food(models.Model):
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    plate_pieces = models.CharField(max_length=50)
    item_img = models.ImageField(upload_to="item_imgs", default="default_food.jpg")

    def __str__(self):
        return self.name
