from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class DishTypeModelTest(TestCase):

    def test_dish_type_str_method(self):
        dish_type = DishType.objects.create(
            name="Test"
        )
        self.assertEqual(str(dish_type), dish_type.name)


class DishModelTest(TestCase):
    def test_dish_model_str_method(self):
        dish_type = DishType.objects.create(
            name="Test"
        )
        dish = Dish.objects.create(
            name="Test",
            description="test test",
            price=100,
            dish_type=dish_type
        )
        self.assertEqual(str(dish), dish.name)


class CookModelTest(TestCase):

    def test_cook_model_str_method(self):
        cook = get_user_model().objects.create(
            username="test",
            password="test123456",
            first_name="Test_f_n",
            last_name="Test_l_n",
            years_of_experience=2
        )
        self.assertEqual(
            str(cook), f"{cook.first_name} {cook.last_name}"
        )
