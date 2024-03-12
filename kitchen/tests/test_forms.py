from django.test import TestCase

from kitchen.forms import (
    RegistrationForm,
    DishTypeNameSearchForm,
    CookLastNameSearchForm,
)


class RegistrationFormTest(TestCase):

    def test_registration_form_with_valid_data(self):
        form_data = {
            "username": "test",
            "first_name": "Test",
            "last_name": "Test",
            "years_of_experience": 2,
            "password1": "test123456",
            "password2": "test123456"
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_registration_form_with_invalid_data(self):
        form_data = {
            "username": "test",
            "first_name": "Test",
            "last_name": "Test",
            "years_of_experience": -2,
            "password1": "test123456",
            "password2": "test123456"
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())


class DishTypeNameSearchFormTest(TestCase):
    def test_form_with_valid_data(self):
        form_data = {"name": "pasta"}
        form = DishTypeNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_when_form_is_empty(self):
        form_data = {}
        form = DishTypeNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class CookLastNameSearchFormTest(TestCase):
    def test_form_with_valid_data(self):
        form_data = {"last_name": "Smith"}
        form = CookLastNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_when_form_is_empty(self):
        form_data = {}
        form = CookLastNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
