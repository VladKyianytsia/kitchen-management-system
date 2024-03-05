from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=65)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
