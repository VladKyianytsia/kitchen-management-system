from django.urls import path

from kitchen.views import (
    register_view,
    index,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeDeleteView,
    DishTypeUpdateView,
    DishDetailView,
    toggle_assign_to_dish,
    DishCreateView,
    DishDeleteView,
    DishUpdateView,
    CookListView,
    CookDetailView,
    CookUpdateView,
)


app_name = "kitchen"

urlpatterns = [
    path("", index, name="index"),
    path(
        "register/",
        register_view,
        name="register"
    ),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-types-list"
    ),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-types/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-types-detail"
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dishes/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign"
    ),
    path(
        "dish-types/<int:pk>/create-dish/",
        DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cooks/<int:pk>/update",
        CookUpdateView.as_view(),
        name="cook-update"
    )
]
