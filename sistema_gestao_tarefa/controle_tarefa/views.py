from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Projeto
from .models import Tag
from django.contrib.auth.models import User

@login_required(login_url='/auth/login')
def projetos(request):
    usuario_logado = request.user
    # projetos_do_usuario = usuario_logado.projetos_criados.all()
    projetos_do_usuario = Projeto.objects.filter(criador=usuario_logado) | Projeto.objects.filter(membros=usuario_logado)
    projetos_do_usuario = projetos_do_usuario.distinct()
    
    template = loader.get_template('projetos.html')
    return HttpResponse(template.render({'user': usuario_logado, 'projetos_do_usuario': projetos_do_usuario}))

@login_required(login_url='/auth/login')
def projeto_excluir(request, id):
    projeto = Projeto.objects.get(id=id)
    projeto.delete()
    return redirect('projetos')


@login_required(login_url='/auth/login')
def projeto_adicionar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        membros_ids = request.POST.getlist('membros')
        tags_ids = request.POST.get('tags').split(',')
        nova_tag_nome = request.POST.get('nova_tag')

        # Criar projeto
        projeto = Projeto.objects.create(
            nome=nome,
            descricao=descricao,
            criador=request.user
        )

        membros = User.objects.filter(id__in=membros_ids)
        projeto.membros.set(membros)

        tags = Tag.objects.filter(id__in=[tid for tid in tags_ids if tid.isdigit()])
        projeto.tags.set(tags)

        if nova_tag_nome:
            nova_tag, created = Tag.objects.get_or_create(nome=nova_tag_nome)
            projeto.tags.add(nova_tag)

        return redirect('projetos') 

    usuarios = User.objects.exclude(id=request.user.id)
    tags = Tag.objects.all()
    return render(request, 'projeto_adicionar.html', {'usuarios': usuarios, 'tags': tags})



@login_required(login_url='/auth/login')
def projeto_detalhes(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == "POST":
        projeto.nome = request.POST.get('nome', projeto.nome)
        projeto.descricao = request.POST.get('descricao', projeto.descricao)
        membros_ids = request.POST.getlist('membros')
        projeto.membros.set(User.objects.filter(id__in=membros_ids))  
        
        nova_tag = request.POST.get('nova_tag', '').strip()
        if nova_tag:
            tag, created = Tag.objects.get_or_create(nome=nova_tag)
            projeto.tags.add(tag)
        projeto.save()
        return HttpResponseRedirect(reverse('projeto_detalhes', args=[projeto.id]))

    # Renderizar a página com as informações do projeto
    return render(request, 'projeto_detalhes.html', {
        'projeto': projeto,
        'usuarios': User.objects.exclude(id=projeto.criador.id)
                                .exclude(is_superuser=True)
                                .exclude(is_staff=True),
        'tags': Tag.objects.all(),
    })
