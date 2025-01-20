from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('projetos/detalhes/<int:id>', views.projeto_detalhes, name='projeto_detalhes'),
    path('projetos/adicionar', views.projeto_adicionar, name='projeto_adicionar'),
    path('projetos/excluir/<int:id>', views.projeto_excluir, name='projeto_excluir'),
]