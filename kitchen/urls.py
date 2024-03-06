from django.urls import path

from kitchen.views import (
    register_view,
    index,
    logout_view,
    DishTypeListView,
)

app_name = "kitchen"

urlpatterns = [
    path("", index, name="index"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list")
]
