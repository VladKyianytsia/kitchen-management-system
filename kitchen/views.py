from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import RegistrationForm, DishTypeForm
from kitchen.models import DishType, Dish


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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    context_object_name = "dish_type"
    template_name = "kitchen/dish_type_detail.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


def dish_type_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    dish_type = DishType.objects.get(pk=pk)
    dish_type.delete()
    return redirect("kitchen:dish-types-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


@login_required
def toggle_assign_to_dish(request: HttpRequest, pk: int) -> HttpResponse:
    dish = Dish.objects.get(pk=pk)
    if (
        request.user in dish.cooks.all()
    ):
        dish.cooks.remove(request.user)
    else:
        dish.cooks.add(request.user)
    return HttpResponseRedirect(reverse_lazy("kitchen:dish-detail", kwargs={"pk": pk}))
