# Generated by Django 5.1.4 on 2024-12-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_tarefa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='projeto',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='projetos', to='controle_tarefa.tag'),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tarefas', to='controle_tarefa.tag'),
        ),
    ]
