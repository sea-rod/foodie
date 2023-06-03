from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate


# Create your tests here.
class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="test123", password="test123"
        )

        return super().setUpTestData()

    def test_user_authenticate(self):
        flag = authenticate(username="test12d3", password="test123")
        self.assertFalse(flag)

        flag = authenticate(username="test123", password="test123")
        self.assertTrue(flag)

    def test_user_login(self):
        flag = self.client.login(username="test123", password="est123")
        self.assertFalse(flag)

        flag = self.client.login(username="test123", password="test123")
        self.assertTrue(flag)

        if flag:
            response = self.client.get(reverse("home"))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "test123")
            self.assertTemplateUsed("index.html")
