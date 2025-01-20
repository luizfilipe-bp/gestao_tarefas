from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('projetos/detalhes/<int:id>', views.projeto_detalhes, name='projeto_detalhes'),
    path('projetos/adicionar', views.adicionar_projeto, name='adicionar_projeto'),
]