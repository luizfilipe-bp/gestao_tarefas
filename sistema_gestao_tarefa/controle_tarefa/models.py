from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos_criados')
    membros = models.ManyToManyField(User, related_name='projetos', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='projetos', blank=True)

    def __str__(self):
        return f'{self.nome} - {self.criador}'


class Tarefa(models.Model):
    STATUS = [
        ('todo', 'To Do'),
        ('em_andamento', 'Em andamento'),
        ('feito', 'Feito'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')
    atribuido_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas')
    status = models.CharField(max_length=20, choices=STATUS, default='todo')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_prazo_final = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tarefas', blank=True)

    def __str__(self):
        return f'{self.titulo} - ({self.status})'