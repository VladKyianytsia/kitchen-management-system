from django.urls import path

from kitchen.views import (
    register_view,
    index,
    logout_view,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    dish_type_delete_view,
    DishTypeUpdateView,
    DishDetailView,
    toggle_assign_to_dish,
    dish_create_view,
    dish_delete_view,
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
    path("logout/", logout_view, name="logout"),
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
        dish_type_delete_view,
        name="dish-type-delete"
    ),
    path(
        "dish/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dish/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign"
    ),
    path(
        "dish-types/<int:pk>/create-dish/",
        dish_create_view,
        name="dish-create"
    ),
    path(
        "dish/<int:pk>/delete/",
        dish_delete_view,
        name="dish-delete"
    ),
    path(
        "dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "cook/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cook/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cook/<int:pk>/update",
        CookUpdateView.as_view(),
        name="cook-update"
    )
]
