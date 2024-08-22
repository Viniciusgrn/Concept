from django.urls import path
from . import views

urlpatterns = [
    path('Sobre', views.index, name='index'),
    path('Orcamento', views.index, name='index'),
    path('Contato', views.index, name='index'),
]


