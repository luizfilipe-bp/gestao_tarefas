from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from .models import Projeto
from .models import Tag
from .models import Tarefa
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
def projeto_detalhes(request, id):
    projeto = Projeto.objects.get(id=id)
    tarefas_do_projeto = Tarefa.objects.filter(projeto=projeto)

    return render(request, 'projeto_detalhes.html', {'projeto': projeto, 'tarefas_do_projeto': tarefas_do_projeto})

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
def projeto_alterar(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == "POST":
        projeto.nome = request.POST.get('nome', projeto.nome).strip()
        projeto.descricao = request.POST.get('descricao', projeto.descricao).strip()
        projeto.save()

        membros_ids = request.POST.get('membros', '')
        membros_ids = [int(mid) for mid in membros_ids.split(',') if mid.isdigit()]
        
        membros_atuais = set(projeto.membros.values_list('id', flat=True))
        novos_membros = set(membros_ids)
        membros_removidos = membros_atuais - novos_membros
        
        projeto.membros.set(User.objects.filter(id__in=membros_ids))

        if membros_removidos:
            Tarefa.objects.filter(projeto=projeto, atribuido_a__id__in=membros_removidos).update(atribuido_a=None)

        tags_input = request.POST.get('tags', '')
        tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
        tag_ids = [int(tag) for tag in tags if tag.isdigit()]
        tags_nomes = [tag for tag in tags if not tag.isdigit()]

        projeto.tags.set(Tag.objects.filter(id__in=tag_ids))
        for tag_nome in tags_nomes:
            tag, _ = Tag.objects.get_or_create(nome=tag_nome)
            projeto.tags.add(tag)

        return HttpResponseRedirect(reverse('projetos'))

    return render(request, 'projeto_alterar.html', {
        'projeto': projeto,
        'usuarios': User.objects.exclude(id=projeto.criador.id)
                                .exclude(is_superuser=True)
                                .exclude(is_staff=True),
        'tags': Tag.objects.all(),
    })



@login_required(login_url='/auth/login')
def tarefas(request):
    usuario_logado = request.user

    tarefas_do_usuario = Tarefa.objects.filter(atribuido_a=usuario_logado).order_by('data_criacao')

    ordenar = request.GET.get('ordenar')
    if ordenar == 'prazo':
        print()
        tarefas_do_usuario = tarefas_do_usuario.order_by('data_prazo_final')

    return HttpResponse(render(request, 'tarefas.html', {'user': usuario_logado, 'tarefas_do_usuario': tarefas_do_usuario}))
    

@login_required(login_url='/auth/login')
def tarefa_adicionar(request, id_projeto):
    projeto = get_object_or_404(Projeto, id=id_projeto)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao', '')
        atribuido_a_id = request.POST.get('atribuido_a')
        status = request.POST.get('status', 'To Do')
        data_prazo_final = request.POST.get('data_prazo_final')
        tags_input = request.POST.get('tags', '')

        atribuido_a = User.objects.filter(id=atribuido_a_id).first() if atribuido_a_id else None

        tarefa = Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            projeto=projeto,
            atribuido_a=atribuido_a,
            status=status,
            data_prazo_final=data_prazo_final
        )

        if tags_input:
            tag_nomes = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
            for nome in tag_nomes:
                tag, created = Tag.objects.get_or_create(nome=nome)
                tarefa.tags.add(tag)

        tarefa.save()
        messages.success(request, 'Tarefa adicionada com sucesso!')
        return redirect('projeto_detalhes', id=projeto.id)

    tags = Tag.objects.all()
    return render(request, 'tarefa_adicionar.html', {'projeto': projeto, 'tags': tags})