import json
import random
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.conf import settings
from django.db import models

# ✅ absolute imports
from recipes.forms import RecipeForm
from recipes.models import Recipe, RecipeIngredient
from recipes.helper import update_recipe_ingredients, to_recipe_data_transfer_objects


@login_required(login_url='/login')
def index(request):
    amount_param = request.GET.get("amount")
    if not amount_param or not amount_param.isnumeric() or not int(amount_param) >= 1:
        amount = settings.DEFAULT_SUGGESTION_AMOUNT
    else:
        amount = int(amount_param)

    data_transfer_objects = to_recipe_data_transfer_objects(
        random.sample(list(Recipe.objects.all()), min(int(amount), Recipe.objects.count()))
    )
    return render(request, "recipes/index.html", {"recipes": data_transfer_objects})


@login_required
def recipe_list(request):
    query = request.GET.get('q', '').strip()
    recipes = Recipe.objects.all()
    if query:
        recipes = recipes.filter(
            models.Q(name__icontains=query) |
            models.Q(ingredients__ingredient__icontains=query)
        ).distinct()
    return render(request, 'recipes/recipelist.html', {
        'recipes': recipes.order_by("name"),
        'textfilter': query
    })


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            update_recipe_ingredients(recipe, request.POST.get('ingredients'))
            return HttpResponseRedirect(reverse('recipe_list'))
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe.html', {
        'mode': 'add',
        'form': form,
        'ingredientsJson': json.dumps([])
    })


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            update_recipe_ingredients(recipe, request.POST.get('ingredients'))
            return HttpResponseRedirect(reverse('recipe_list'))
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/recipe.html', {
        'mode': 'edit',
        'context': recipe,
        'form': form,
        'ingredientsJson': json.dumps([
            {"amount": x.amount, "unit": x.unit, "ingredient": x.ingredient}
            for x in RecipeIngredient.objects.filter(recipe=recipe)
        ])
    })
