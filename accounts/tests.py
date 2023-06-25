from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, authenticate
from .models import CustomerAddress


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
            response = self.client.get(reverse_lazy("home"))
            self.assertEqual(response.status_code, 200)

            self.assertContains(response, "test123")
            self.assertTemplateUsed("index.html")

    def test_user_profile(self):
        self.user.email = "test123@gmail.com"
        self.user.save()
        reponse = self.client.get(reverse_lazy("profile", kwargs={"pk": self.user.pk}))
        self.assertAlmostEqual("test123", reponse.context["form"]["username"].value())
        self.assertAlmostEqual(
            "test123@gmail.com", reponse.context["form"]["email"].value()
        )

    def test_create_cutomer_address(self):
        address = CustomerAddress.objects.get(user=self.user)
        address.pincode = 123456
        address.ward = "testward"
        address.village_city = "testcity"
        address.landmark = "testlandmark"
        address.house_no = "11_22"
        address.save()

        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy("address_settings"))
        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "settings.html")

        self.assertAlmostEqual("testward", response.context["form"]["ward"].value())
        self.assertAlmostEqual(
            "testcity", response.context["form"]["village_city"].value()
        )
        self.assertAlmostEqual(
            "testlandmark", response.context["form"]["landmark"].value()
        )
        self.assertAlmostEqual("11_22", response.context["form"]["house_no"].value())
        self.assertAlmostEqual(123456, response.context["form"]["pincode"].value())
