"""djangodelights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('ingredients/', views.IngredientsView.as_view(), name="ingredients"),
    path('ingredients/new', views.NewIngredientView.as_view(), name="add_ingredient"),

    path('menu/', views.MenuView.as_view(), name="menu"),
    path('menu/new', views.NewMenuItemView.as_view(), name="add_menu_item"),
    path('reciperequirement/new', views.NewRecipeRequirementView.as_view(), name="add_recipe_requirement"),

    path('purchases/', views.purchases, name="purchases"),
    path('revenue/', views.revenue, name="revenue"),
    path('account/', views.logout, name="logout"),
    path("account/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
