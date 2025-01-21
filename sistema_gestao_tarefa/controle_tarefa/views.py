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
        membros_ids = request.POST.get('membros', '')
        tags_nomes = request.POST.get('tags', '').split(',')

        # Criar projeto
        projeto = Projeto.objects.create(
            nome=nome,
            descricao=descricao,
            criador=request.user
        )

        # Associar membros
        membros_ids = [int(mid) for mid in membros_ids.split(',') if mid.isdigit()]
        membros = User.objects.filter(id__in=membros_ids)
        projeto.membros.set(membros)

        # Processar tags (verificar se existe ou criar nova, evitando tags vazias)
        for tag_nome in tags_nomes:
            tag_nome = tag_nome.strip()
            if tag_nome:  # Apenas processa se o nome da tag não estiver vazio
                tag, _ = Tag.objects.get_or_create(nome=tag_nome)
                projeto.tags.add(tag)

        return redirect('projetos')

    usuarios = User.objects.exclude(id=request.user.id).exclude(is_superuser=True).exclude(is_staff=True)
    tags = Tag.objects.all()
    return render(request, 'projeto_adicionar.html', {'usuarios': usuarios, 'tags': tags})



@login_required(login_url='/auth/login')
def projeto_detalhes(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == "POST":
        projeto.nome = request.POST.get('nome', projeto.nome).strip()
        projeto.descricao = request.POST.get('descricao', projeto.descricao).strip()
        projeto.save()

        membros_ids = request.POST.get('membros', '')
        membros_ids = [int(mid) for mid in membros_ids.split(',') if mid.isdigit()]
        projeto.membros.set(User.objects.filter(id__in=membros_ids))

        tags_input = request.POST.get('tags', '')  
        tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()] 

        tag_ids = [int(tag) for tag in tags if tag.isdigit()]  
        tags_nomes = [tag for tag in tags if not tag.isdigit()]  

        projeto.tags.set(Tag.objects.filter(id__in=tag_ids))

        for tag_nome in tags_nomes:
            tag, _ = Tag.objects.get_or_create(nome=tag_nome)
            projeto.tags.add(tag)

        return HttpResponseRedirect(reverse('projeto_detalhes', args=[projeto.id]))

    return render(request, 'projeto_detalhes.html', {
        'projeto': projeto,
        'usuarios': User.objects.exclude(id=projeto.criador.id)
                                .exclude(is_superuser=True)
                                .exclude(is_staff=True),
        'tags': Tag.objects.all(),
    })