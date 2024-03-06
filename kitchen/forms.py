from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxSelectMultiple

from kitchen.models import Dish, DishType


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience"
        )


class DishTypeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = DishType
        fields = "__all__"


class DishForm(forms.ModelForm):
    dish_type = forms.ModelChoiceField(
        disabled=True,
        queryset=DishType.objects.all(),
    )

    class Meta:
        model = Dish
        fields = ("name", "description", "price", "dish_type",)


class CookYearsOfExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("years_of_experience",)
