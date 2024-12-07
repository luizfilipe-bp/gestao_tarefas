from django.contrib import admin
from .models import Projeto
from .models import Tarefa
from .models import Tag

admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(Tag)