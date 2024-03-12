from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import (
    RegistrationForm,
    DishTypeForm,
    DishForm,
    CookUpdateForm,
    DishTypeNameSearchForm,
    CookLastNameSearchForm
)
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

    form = RegistrationForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.save()
        login(request, user)
        return redirect("kitchen:index")

    return render(
        request,
        "kitchen/cook_registration.html",
        context={
            "form": form
        }
    )


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(
            DishTypeListView, self
        ).get_context_data(**kwargs)

        context["search_form"] = DishTypeNameSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        queryset = super().get_queryset()
        if name:
            return queryset.filter(name__icontains=name)

        return queryset


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


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-types-list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.prefetch_related("cooks")


@login_required
def toggle_assign_to_dish(
        request: HttpRequest,
        pk: int
) -> HttpResponse:
    dish = Dish.objects.get(pk=pk)
    if (
        request.user in dish.cooks.all()
    ):
        dish.cooks.remove(request.user)
    else:
        dish.cooks.add(request.user)
    return HttpResponseRedirect(
        reverse_lazy(
            "kitchen:dish-detail",
            kwargs={"pk": pk}
        )
    )


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'kitchen/dish_form.html'
    form_class = DishForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'dish_type': self.get_dish_type()}
        return kwargs

    def get_success_url(self):
        return reverse_lazy(
            "kitchen:dish-types-detail",
            kwargs={"pk": self.get_dish_type().pk}
        )

    def get_dish_type(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(DishType, pk=pk)

    def form_valid(self, form):
        dish = form.save(commit=False)
        dish.dish_type = self.get_dish_type()
        dish.save()
        return super().form_valid(form)


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish

    def get_success_url(self):
        return reverse_lazy(
            "kitchen:dish-types-detail",
            kwargs={"pk": self.object.dish_type.pk}
        )

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm

    def get_success_url(self):
        return reverse_lazy(
            "kitchen:dish-detail",
            kwargs={"pk": self.object.pk}
        )


class CookListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)

        context["search_form"] = CookLastNameSearchForm()
        return context

    def get_queryset(self):
        last_name = self.request.GET.get("last_name")
        queryset = super().get_queryset()
        if last_name:
            return queryset.filter(last_name__icontains=last_name)

        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = CookUpdateForm

    def get_success_url(self):
        return reverse_lazy(
            "kitchen:cook-detail",
            kwargs={"pk": self.object.pk}
        )
