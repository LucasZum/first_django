from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'recipes/pages/home.html', context={
        'name': 'Lucas Queiroz'
    })


def about(req):
    return HttpResponse("WELCOME TO ABOUT PAGE!!!")
