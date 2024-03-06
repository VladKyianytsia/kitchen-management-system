from django.urls import path

from kitchen.views import register, index

app_name = "kitchen"

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
]
