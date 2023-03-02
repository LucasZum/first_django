from django.shortcuts import render

from utils.recipes.factory import make_recipe


def home(req):
    return render(req, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(9)],
    })


def recipes(req, id):
    return render(req, 'recipes/pages/recipes-view.html', context={
        'recipe': make_recipe(),
        'is_recipe_page': True
    })
