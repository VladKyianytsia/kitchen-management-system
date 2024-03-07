from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Dish, DishType


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience"
        )

    def clean_years_of_experience(self):
        return years_of_experience_validator(
            self.cleaned_data["years_of_experience"]
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

    def clean_years_of_experience(self):
        return years_of_experience_validator(
            self.cleaned_data["years_of_experience"]
        )


class DishTypeNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class CookLastNameSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by last name"
            }
        )
    )


def years_of_experience_validator(
        years_of_experience: int
) -> ValidationError | int:
    if years_of_experience < 0:
        raise forms.ValidationError("Invalid data")
    return years_of_experience
