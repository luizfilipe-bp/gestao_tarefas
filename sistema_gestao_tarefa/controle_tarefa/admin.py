from django.contrib import admin
from .models import Projeto
from .models import Tarefa
from .models import Tag

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'criador', 'data_criacao')

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'status')

class TagAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Tag, TagAdmin)