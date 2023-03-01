from django.urls import path
from recipes.views import home, about


urlpatterns = [
    path('', home),
    path('about/', about)
]