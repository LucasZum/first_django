from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'recipes/index.html', context={
        'name': 'Lucas'
    })


def about(req):
    return HttpResponse("THIS IS ABOUT PAGE, WELCOME!!!")
