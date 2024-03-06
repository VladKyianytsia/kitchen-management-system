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
    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = DishType
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if DishType.objects.filter(name=name).exists():
            raise forms.ValidationError("This category is already exists")
        return name
