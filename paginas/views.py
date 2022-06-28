from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.shortcuts import render

#método para editar os usuários
from usuarios.models import PerfilAluno, PerfilCoordenador

#método para editar os cadastros
from cadastros.models import Curso, Turma

# Autenticando com Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# User
from django.contrib.auth.models import User


class IndexView(ListView):
    models = Curso
    template_name = 'index.html'
    queryset = Curso.objects.filter(nivel='Superior')
    context_object_name = 'texto'

############ Barra de menu #################
class EgressoAreaView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    group_required = u'Egresso'
    template_name = 'pegresso_gerenciar.html'

class CoordenadorAreaView(GroupRequiredMixin,LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    group_required = u'Coordenador'
    template_name = 'pcoordenador_gerenciar.html'


############# Navegação na página ####################
def listacursosview(request, curso_id):
    indexcursos = Curso.objects.filter(nivel=curso_id)
    return render(request, 'listacursos.html', { "indexcursos" : indexcursos})


def listarturmasview(request, turma_id):
    turmas2 = Turma.objects.filter(curso=turma_id)
    return render(request, 'listaturmas.html', { "turmas2" : turmas2})


def listaregressoview(request, egresso_id):

    egressos1 = PerfilAluno.objects.filter(turma=egresso_id)
    return render(request, 'listaegresso.html', { "egressos1" : egressos1})


############# Página do coordenador ####################
def GerenciarAlunos2View(request):
    usuario_logado = request.user.perfilcoordenador.curso.id
    gerenciaralunos2 = PerfilAluno.objects.filter(curso=usuario_logado)
    return render(request, 'gerenciar_alunos.html', { "gerenciaralunos2" : gerenciaralunos2})
