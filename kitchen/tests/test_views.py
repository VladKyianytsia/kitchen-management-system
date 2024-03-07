from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import DishType, Dish


class RegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration_get(self):
        response = self.client.get(reverse("kitchen:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("kitchen/cook_registration.html")

    def test_registration_post_with_valid_data(self):
        data = {
            "username": "test",
            "password1": "test123456",
            "password2": "test123456",
            "years_of_experience": 2
        }
        response = self.client.post(reverse("kitchen:register"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            get_user_model().objects.filter(username="test").exists()
        )

    def test_registration_post_with_invalid_data(self):
        data = {
            "username": "test",
            "password1": "test123",
            "password2": "test123",
        }
        response = self.client.post(reverse("kitchen:register"), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            get_user_model().objects.filter(username="test").exists()
        )


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123456",
            years_of_experience=1
        )

    def test_logout(self):
        self.client.login(username="test", password="test123456")
        response = self.client.get(reverse("kitchen:logout"))
        self.assertEqual(response.status_code, 302)
        self.assertFalse("_auth_user_id" in self.client.session)


class TestDishTypeDeleteView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123456",
            years_of_experience=1
        )
        self.client.login(username="test", password="test123456")
        self.dish_type = DishType.objects.create(
            name="TestDishType"
        )

    def test_dish_type_delete(self):
        response = self.client.post(
            reverse(
                "kitchen:dish-type-delete",
                kwargs={"pk": self.dish_type.id}
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            DishType.objects.filter(pk=self.dish_type.id).exists()
        )


class ToggleAssignToDishViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123456",
            years_of_experience=1
        )
        self.client.login(
            username="test",
            password="test123456"
        )
        self.dish = Dish.objects.create(
            name="TestDish",
            dish_type=DishType.objects.create(
                name="TestDishType"
            ),
            price=10,
            description="test description"
        )

    def test_toggle_assign_add(self):
        response = self.client.post(
            reverse(
                "kitchen:toggle-dish-assign",
                kwargs={"pk": self.dish.id}
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            self.dish.cooks.filter(pk=self.user.id).exists()
        )

    def test_toggle_assign_remove(self):
        self.dish.cooks.add(self.user)
        response = self.client.post(
            reverse(
                "kitchen:toggle-dish-assign",
                kwargs={"pk": self.dish.id}
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            self.dish.cooks.filter(pk=self.user.id).exists()
        )
