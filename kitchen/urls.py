from django.urls import path

from kitchen.views import (
    register_view,
    index,
    logout_view,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    dish_type_delete_view,
)

app_name = "kitchen"

urlpatterns = [
    path("", index, name="index"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-types-detail"),
    path("dish-types/<int:pk>/delete", dish_type_delete_view, name="dish-type-delete")
]
