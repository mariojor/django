from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pessoas, name='lista_pessoas'),
    path('meuApp/', views.adiciona_pessoa, name='adiciona_pessoa'),
]
