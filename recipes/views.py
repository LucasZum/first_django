from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipe


def home(req):
    return render(req, 'recipes/pages/home.html', context={
        'recipes': Recipe.objects.filter(
            is_published=True
        ).order_by('-id')
    })


def category(req, category_id):

    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id')

    if not recipes:
        return HttpResponse('Not Found', status=404)

    return render(req, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} | Category'
    })


def recipe(req, id):

    recipe = Recipe.objects.filter(
        id=id,
        is_published=True,
    ).order_by('-id').first()

    if not recipe:
        return HttpResponse('Nenhuma receita encontrada!', status=404)

    return render(req, 'recipes/pages/recipes-view.html', context={
        'is_recipe_page': True,
        'recipe': recipe
    })
