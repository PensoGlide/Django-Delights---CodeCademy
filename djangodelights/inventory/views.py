from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView

# Create your views here.
@login_required
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
    template_name = "registration/signup.html"