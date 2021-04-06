from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('minha-consulta', views.minha_consulta, name='minha_consulta'),

]