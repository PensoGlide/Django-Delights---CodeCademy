from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView

# Create your views here.
#@login_required BASTA TIRAR ISTO DOS COMENTARIOS PARA VOLTAR A SER A PRIMEIRA PAGINA
def home(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/home.html", username)

def ingredients(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/ingredients.html", username)

def menu(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/menu.html", username)

def purchases(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/purchases.html", username)

def revenue(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/revenue.html", username)

def logout(request):
    username = {"name": "Rasco"}
    logout(request)
    return redirect("login")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"