from django.contrib import admin
from .models import Projeto
from .models import Tarefa

admin.site.register(Projeto)
admin.site.register(Tarefa)