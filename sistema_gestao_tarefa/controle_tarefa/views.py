from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login')
def projetos(request):
    usuario_logado = request.user
    
    template = loader.get_template('projetos.html')
    return HttpResponse(template.render({'user': usuario_logado}))