from django.urls import path
from . import views

urlpatterns = [
    # Home & Recipes (HTML pages)
    path("", views.index, name="index"),
    path("recipes/", views.recipe_list, name="recipe_list"),
    path("recipes/add/", views.add_recipe, name="add_recipe"),
    path("recipes/<int:recipe_id>/edit/", views.edit_recipe, name="edit_recipe"),

    # API Endpoints (JSON)
    path("api/recipes/<int:page_no>/", views.recipes_api, name="recipes_api"),
    path("api/recipe/", views.recipe_api, name="recipe_api"),
    path("api/language/", views.language_api, name="language_api"),

    # Authentication
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]
