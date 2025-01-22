from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('projetos/alterar/<int:id>', views.projeto_alterar, name='projeto_alterar'),
    path('projetos/adicionar', views.projeto_adicionar, name='projeto_adicionar'),
    path('projetos/excluir/<int:id>', views.projeto_excluir, name='projeto_excluir'),
    path('projetos/detalhes/<int:id>', views.projeto_detalhes, name='projeto_detalhes'),
    path('tarefas', views.tarefas, name='tarefas')
]