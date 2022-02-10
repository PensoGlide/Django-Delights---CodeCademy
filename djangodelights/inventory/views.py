from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/home.html", username)

def ingredients(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/home.html", username)

def menu(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/home.html", username)

def purchases(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/home.html", username)

def revenue(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/home.html", username)

def logout(request):
    username = {"name": "Rasco"}
    return render(request, "inventory/home.html", username)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "inventory/login.html"