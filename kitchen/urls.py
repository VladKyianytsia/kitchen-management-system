from django.urls import path

from kitchen.views import register

app_name = "kitchen"

urlpatterns = [
    path("register/", register, name="register")
]
