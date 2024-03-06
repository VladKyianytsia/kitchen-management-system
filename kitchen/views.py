from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from kitchen.forms import RegistrationForm


@login_required
def index(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "kitchen/index.html")


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = RegistrationForm()
        return render(
            request,
            "kitchen/cook_registration.html",
            context={
                "form": form
            }
        )
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect("kitchen:index")
        else:
            return render(
                request,
                "kitchen/cook_registration.html",
                context={
                    "form": form
                }
            )


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("login")
