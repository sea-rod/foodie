from django.test import TestCase
from django.urls import reverse
from .models import Food, FoodCategory


class FoodTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.food_category = FoodCategory.objects.create(name="Starters")
        cls.food = Food.objects.create(
            food_category=cls.food_category,
            name="french Fries",
            price=120,
            plate_pieces=1,
        )
        return super().setUpTestData()

    def test_menu_template(self):
        reponse = self.client.get(reverse("menu"))
        self.assertAlmostEqual(
            self.food_category.name, reponse.context["food_category"][0].name
        )
