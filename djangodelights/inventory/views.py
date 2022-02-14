from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView

from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm

# Create your views here.
@login_required #BASTA TIRAR ISTO DOS COMENTARIOS PARA VOLTAR A SER A PRIMEIRA PAGINA
def home(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/home.html", username)

class IngredientsView(LoginRequiredMixin, ListView):
    template_name = "inventory/ingredients.html"
    model = Ingredient

class NewIngredientView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_ingredient.html"
    model = Ingredient
    form_class = IngredientForm

class MenuView(LoginRequiredMixin, ListView):
    template_name = "inventory/menu.html"
    model = MenuItem

def purchases(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/purchases.html", username)

def revenue(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/revenue.html", username)

class NewMenuItemView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_menu_item.html"
    model = MenuItem
    form_class = MenuItemForm


class NewRecipeRequirementView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_recipe_requirement.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm


def logout(request):
    username = {"name": "Rasco"}
    logout(request)
    return redirect("login")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"